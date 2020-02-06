# ###############################################################
# ALIASES: stack 
# ###############################################################

# Stack commands.
alias stests-stack-setup=$STESTS_PATH_SH/stack_setup.sh
alias stests-stack-update=$STESTS_PATH_SH/stack_update.sh

# ###############################################################
# ALIASES: workers
# ###############################################################

# Workers commands.
alias stests-workers-run=$STESTS_PATH_SH/workers/run.sh
alias stests-workers-stop=$STESTS_PATH_SH/workers/stop.sh
alias stests-workers-reload=$STESTS_PATH_SH/workers/reload.sh
alias stests-workers-status=$STESTS_PATH_SH/workers/status.sh
alias stests-workers-reset-logs=$STESTS_PATH_SH/workers/reset_logs.sh

# ###############################################################
# ALIASES: cache
# ###############################################################

# Cache interaction commands.
alias stests-set-network='cd $STESTS_HOME && pipenv run python $STESTS_PATH_CLI/cache/set_network.py'
alias stests-set-network-faucet-key='cd $STESTS_HOME && pipenv run python $STESTS_PATH_CLI/cache/set_network_faucet_key.py'
alias stests-set-node='cd $STESTS_HOME && pipenv run python $STESTS_PATH_CLI/cache/set_node.py'
alias stests-set-node-bonding-key='cd $STESTS_HOME && pipenv run python $STESTS_PATH_CLI/cache/set_node_bonding_key.py'

# ###############################################################
# ALIASES: generators
# ###############################################################

_exec_generator()
{
    # Destructure generator type, pahse & args.
    args=($@)
    args_len=${#args[@]}
    g_type=${args[0]}
    g_phase=${args[1]}
    g_args=${args[@]:2:$args_len}

    # Execute generator.
    pipenv run python $STESTS_PATH_GENERATORS/wg_$g_type $g_args
}

# WG-100: ERC-20 auction.
alias stests-wg-100='_exec_generator 100'