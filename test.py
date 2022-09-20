from run_attacks import test
from utils import parse_args, compute_run_args, compute_data_args, compute_VO_args, compute_attack_args, \
    compute_output_dir


def define_args():
    args = parse_args()

    # running args
    args.seed = 42
    args.save_csv = True
    args.run_name = 'new'
    args.save_best_pert = True
    args.preprocessed_data = True
    args.cross_validation = False

    # data args
    args.max_traj_len = 8

    # attack args
    args.attack = 'pgd'  # the optimizer
    args.alpha = 0.05
    args.attack_k = 100  # epochs num
    args.attack_t_crit = 'mean_partial_rms'  # train loss
    args.attack_rot_crit = 'quat_product'  # rotation criterion
    args.attack_flow_crit = 'mse'  # flow criterion
    args.attack_target_t_crit = 'patch'  # the projection on the patch
    args.attack_t_factor = 1  # translation factor
    args.attack_rot_factor = 0  # rotation factor
    args.attack_flow_factor = 0  # flow factor
    args.attack_target_t_factor = 0  # the projection on the patch factor
    args.early_stopping = 5

    return args


if __name__ == '__main__':
    # alpha test
    for i in range(1, 6):
        args = define_args()
        args.alpha = 0.01 * i * 2
        args.run_name = f'alpha{args.alpha}'

        args = compute_run_args(args)
        args = compute_data_args(args)
        args = compute_VO_args(args)
        args = compute_attack_args(args)
        args = compute_output_dir(args)

        test(args)

    # # rms test
    # args = define_args()
    # args.attack_t_crit = "rms"
    # args.run_name = f'rms'
    #
    # args = compute_run_args(args)
    # args = compute_data_args(args)
    # args = compute_VO_args(args)
    # args = compute_attack_args(args)
    # args = compute_output_dir(args)
    #
    # test(args)
    #
    # # rot test
    # for i in range(1, 6):
    #     args = define_args()
    #     args.attack_rot_factor = 0.01 * i
    #     args.run_name = f'attack_rot_factor{args.attack_rot_factor}'
    #
    #     args = compute_run_args(args)
    #     args = compute_data_args(args)
    #     args = compute_VO_args(args)
    #     args = compute_attack_args(args)
    #     args = compute_output_dir(args)
    #
    #     test(args)
    #
    # # flow test
    # for i in range(1, 6):
    #     args = define_args()
    #     args.attack_flow_factor = 0.01 * i
    #     args.run_name = f'attack_flow_factor{args.attack_flow_factor}'
    #
    #     args = compute_run_args(args)
    #     args = compute_data_args(args)
    #     args = compute_VO_args(args)
    #     args = compute_attack_args(args)
    #     args = compute_output_dir(args)
    #
    #     test(args)
    #
    # # attack_target_t test
    # for i in range(1, 6):
    #     args = define_args()
    #     args.attack_target_t_factor = 0.01 * i
    #     args.run_name = f'attack_target_t_factor{args.attack_target_t_factor}'
    #
    #     args = compute_run_args(args)
    #     args = compute_data_args(args)
    #     args = compute_VO_args(args)
    #     args = compute_attack_args(args)
    #     args = compute_output_dir(args)
    #
    #     test(args)



