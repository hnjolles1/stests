# ###############################################################
# Helper function
# ###############################################################

function _exec_cmd()
{
    # Destructure command script & args.
    args=($@)
    args_len=${#args[@]}
    s_path=${args[0]}
    s_args=${args[@]:1:$args_len}

    # Execute script.
    pushd $STESTS_HOME
    pipenv run python $s_path $s_args
    popd
}

# ###############################################################
# ALIASES: stack 
# ###############################################################

alias stests-stack-update=$STESTS_PATH_SH/stack/update.sh

# ###############################################################
# ALIASES: workers
# ###############################################################

alias stests-workers-start=$STESTS_PATH_SH/workers/start.sh
alias stests-workers-status=$STESTS_PATH_SH/workers/status.sh
alias stests-workers-stop=$STESTS_PATH_SH/workers/stop.sh
alias stests-workers-reload=$STESTS_PATH_SH/workers/reload.sh
alias stests-workers-reset-logs=$STESTS_PATH_SH/workers/reset_logs.sh

# ###############################################################
# ALIASES: cache
# ###############################################################

alias stests-set-network='_exec_cmd $STESTS_PATH_CLI/cache/set_network.py'
alias stests-set-network-faucet-key='_exec_cmd $STESTS_PATH_CLI/cache/set_network_faucet_key.py'
alias stests-set-node='_exec_cmd $STESTS_PATH_CLI/cache/set_node.py'
alias stests-set-node-bonding-key='_exec_cmd $STESTS_PATH_CLI/cache/set_node_bonding_key.py'

# ###############################################################
# ALIASES: generators
# ###############################################################

function _exec_generator()
{
    # Destructure generator type & args.
    args=($@)
    args_len=${#args[@]}
    g_type=${args[0]}
    g_args=${args[@]:1:$args_len}


    # Execute generator.
    log "workload generator WG-"$g_type
    _exec_cmd $STESTS_PATH_GENERATORS/wg_$g_type $g_args
    log "... execution complete"
}

# WG-100: ERC-20 auction.
alias stests-wg-100='_exec_generator 100'
