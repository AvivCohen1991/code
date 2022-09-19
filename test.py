from run_attacks import test
from utils import parse_args, compute_run_args, compute_data_args, compute_VO_args, compute_attack_args, \
    compute_output_dir

if __name__ == '__main__':
    args = parse_args()

    # running args
    args.seed = 42
    args.save_csv = True
    args.run_name = 'new'
    args.save_best_pert = True
    args.preprocessed_data = True
    args.cross_validation = False

    # data args
    args.max_traj_len = 3

    # attack args
    args.attack = 'apgd'                        # the optimizer
    args.attack_k = 2                           # epochs num
    args.attack_t_crit = 'mean_partial_rms'     # train loss
    args.attack_rot_crit = 'quat_product'       # rotation criterion
    args.attack_flow_crit = 'mse'               # flow criterion
    args.attack_target_t_crit = 'patch'         # the projection on the patch
    args.attack_t_factor = 1                    # translation factor
    args.attack_rot_factor = 0                  # rotation factor
    args.attack_flow_factor = 0                 # flow factor
    args.attack_target_t_factor = 0             # the projection on the patch factor

    for i in range(2):
        args.attack_rot_factor = 1 - i / 4
        print(f'__________________________________rot factor: {args.attack_rot_factor}________________________________')
        args.run_name = f'rotFactor{args.attack_rot_factor}'

        args = compute_run_args(args)
        args = compute_data_args(args)
        args = compute_VO_args(args)
        args = compute_attack_args(args)
        args = compute_output_dir(args)

        test(args)
