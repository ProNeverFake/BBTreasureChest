#include<iostream>
#include<vector>
#include<Eigen/Dense>
#include<cmath>
#include<functional>

Eigen::VectorXd systemModel(const Eigen::VectorXd &x, const Eigen::VectorXd &u){
    Eigen::MatrixXd A(2, 2);
    Eigen::MatrixXd B(2, 1);

    A << 1, 1,
        0, 1;
    B << 0.5,
        1;
    
    Eigen::VectorXd x_next = A*x + B*u;
    return x_next;
}

double objectiveFunction(const Eigen::VectorXd &x, const Eigen::VectorXd &u, const Eigen::VectorXd &x_ref){
    Eigen::MatrixXd Q(2, 2);
    Eigen::MatrixXd R(1, 1);

    Q << 1, 0,
        0, 1;
    R << 1;

    Eigen::VectorXd x_error = x - x_ref;
    double cost = x_error.transpose()*Q*x_error + u.transpose()*R*u;
    return cost;
}

Eigen::VectorXd optimizeControl(const Eigen::VectorXd &x, const Eigen::VectorXd &x_ref, double learning_rate = 0.01, int max_iters = 100){
    Eigen::VectorXd u = Eigen::VectorXd::Zero(1);

    for (int iter = 0; i < max_iters; i++){
        double epslion = 1e-5;
        Eigen::VectorXd u_grad(1);
        Eigen::VectorXd u_temp = u;

        u_temp(0) += epsilon;
        double cost_plus = objectiveFunction(systemModel(x, u_temp), u_temp, x_ref);
        u_temp(0) -= 2*epsilon;
        double cost_minus = objectiveFunction(systemModel(x, u_temp), u_temp, x_ref);

        u_grad(0) = (cost_plus - cost_minux)/(2 * epsilon);

        u -= learning_rate * u_grad;

    }

    return u;
}

int main(){
    Eigen::VectorXd x(2);
    x << 0, 0;

    Eigen::VectorXd x_ref(2);
    x_ref << 1, 0;

    for (int t = 0; t < 10; t++){
        Eigen::VectorXd u = optimizeControl(x, x_ref);
        x = systemModel(x, u);

        std::cout << "Time step " << t << ": u =  " << u(0) << ", x = [" << x(0) << ", " << x(1) << "]" << std::endl;
    }

    return 0;
}
