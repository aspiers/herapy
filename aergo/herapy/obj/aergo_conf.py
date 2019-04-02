
########################################
# !!!DO NOT MODIFY THIS FILE DIRECTLY!!!
########################################
#
# This file is generated by 'generate_aergo_conf.py'.
#
AERGO_CONF_KEYS = {
    "base": ["datadir", "dbtype", "enableprofile", "profileport", "enabletestmode", "usetestnet", "personal", "authdir", ],
    "rpc": ["netserviceaddr", "netserviceport", "netservicetrace", "nstls", "nscert", "nskey", "nsallowcors", ],
    "p2p": ["netprotocoladdr", "netprotocolport", "npbindaddr", "npbindport", "nptls", "npcert", "npkey", "npaddpeers", "nphiddenpeers", "npdiscoverpeers", "npmaxpeers", "nppeerpool", "npexposeself", "npusepolaris", "npaddpolarises", "logfullpeerid", ],
    "polaris": ["allowprivate", "genesisfile", ],
    "blockchain": ["maxblocksize", "coinbaseaccount", "maxanchorcount", "verifiercount", "forceresetheight", "zerofee", ],
    "mempool": ["showmetrics", "enablefadeout", "fadeoutperiod", "verifiers", "dumpfilepath", ],
    "consensus": ["enablebp", "blockinterval", "raft", ],
    "monitor": ["protocol", "endpoint", ],
    "account": ["unlocktimeout", ],
}

AERGO_DEFAULT_CONF = {
    "datadir": "${AERGO_HOME}/data",
    "dbtype": "badgerdb",
    "enableprofile": False,
    "profileport": 6060,
    "enabletestmode": False,
    "personal": True,
    "authdir": "${AERGO_HOME}/auth",
    "rpc": {
        "netserviceaddr": "127.0.0.1",
        "netserviceport": 7845,
        "netservicetrace": False,
        "nstls": False,
        "nskey": "",
    },
    "p2p": {
        "netprotocoladdr": "",
        "netprotocolport": 7846,
        "npbindaddr": "",
        "npbindport": -1,
        "nptls": False,
        "npcert": "",
        "npkey": "",
        "npaddpeers": [],
        "npdiscoverpeers": True,
        "npmaxpeers": 100,
        "nppeerpool": 100,
        "npexposeself": True,
        "npusepolaris": True,
        "npaddpolarises": [],
    },
    "polaris": {
        "allowprivate": False,
        "genesisfile": "",
    },
    "blockchain": {
        "maxblocksize": 1048576,
        "coinbaseaccount": "",
        "maxanchorcount": 20,
        "forceresetheight": 0,
    },
    "mempool": {
        "showmetrics": False,
        "enablefadeout": False,
        "fadeoutperiod": 12,
        "dumpfilepath": "${AERGO_HOME}/mempool.dump",
    },
    "consensus": {
        "enablebp": False,
        "blockinterval": 1,
    },
    "monitor": {
        "protocol": "",
        "endpoint": "",
    },
    "account": {
        "unlocktimeout": 60,
    },
}


class AergoConfig:
    def __init__(self):
        self.__conf = dict(AERGO_DEFAULT_CONF)
        self.__conf['rpc'] = dict(AERGO_DEFAULT_CONF['rpc'])
        self.__conf['p2p'] = dict(AERGO_DEFAULT_CONF['p2p'])
        self.__conf['polaris'] = dict(AERGO_DEFAULT_CONF['polaris'])
        self.__conf['blockchain'] = dict(AERGO_DEFAULT_CONF['blockchain'])
        self.__conf['mempool'] = dict(AERGO_DEFAULT_CONF['mempool'])
        self.__conf['consensus'] = dict(AERGO_DEFAULT_CONF['consensus'])
        self.__conf['monitor'] = dict(AERGO_DEFAULT_CONF['monitor'])
        self.__conf['account'] = dict(AERGO_DEFAULT_CONF['account'])

    def add_conf(self, k, v, c="base"):
        exist = False
        for key in AERGO_CONF_KEYS[c]:
            if key == k:
                exist = True
                break

        if not exist:
            raise KeyError("cannot find a configuration key: " + k)

        if c == "base":
            self.__conf[k] = v
        else:
            self.__conf[c][k] = v

    @property
    def conf(self):
        return self.__conf

    @property
    def datadir(self):
        return str(self.__conf['datadir'])

    @datadir.setter
    def datadir(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['datadir'] = v

    @property
    def dbtype(self):
        return str(self.__conf['dbtype'])

    @dbtype.setter
    def dbtype(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['dbtype'] = v

    @property
    def enableprofile(self):
        return bool(self.__conf['enableprofile'])

    @enableprofile.setter
    def enableprofile(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['enableprofile'] = v

    @property
    def profileport(self):
        return int(self.__conf['profileport'])

    @profileport.setter
    def profileport(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['profileport'] = v

    @property
    def enabletestmode(self):
        return bool(self.__conf['enabletestmode'])

    @enabletestmode.setter
    def enabletestmode(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['enabletestmode'] = v

    @property
    def usetestnet(self):
        return bool(self.__conf['usetestnet'])

    @usetestnet.setter
    def usetestnet(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['usetestnet'] = v

    @property
    def personal(self):
        return bool(self.__conf['personal'])

    @personal.setter
    def personal(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['personal'] = v

    @property
    def authdir(self):
        return str(self.__conf['authdir'])

    @authdir.setter
    def authdir(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['authdir'] = v

    @property
    def rpc(self):
        return self.__conf['rpc']

    @property
    def rpc_netserviceaddr(self):
        return str(self.__conf['rpc']['netserviceaddr'])

    @rpc_netserviceaddr.setter
    def rpc_netserviceaddr(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['rpc']['netserviceaddr'] = v

    @property
    def rpc_netserviceport(self):
        return int(self.__conf['rpc']['netserviceport'])

    @rpc_netserviceport.setter
    def rpc_netserviceport(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['rpc']['netserviceport'] = v

    @property
    def rpc_netservicetrace(self):
        return bool(self.__conf['rpc']['netservicetrace'])

    @rpc_netservicetrace.setter
    def rpc_netservicetrace(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['rpc']['netservicetrace'] = v

    @property
    def rpc_nstls(self):
        return bool(self.__conf['rpc']['nstls'])

    @rpc_nstls.setter
    def rpc_nstls(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['rpc']['nstls'] = v

    @property
    def rpc_nscert(self):
        return str(self.__conf['rpc']['nscert'])

    @rpc_nscert.setter
    def rpc_nscert(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['rpc']['nscert'] = v

    @property
    def rpc_nskey(self):
        return str(self.__conf['rpc']['nskey'])

    @rpc_nskey.setter
    def rpc_nskey(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['rpc']['nskey'] = v

    @property
    def rpc_nsallowcors(self):
        return bool(self.__conf['rpc']['nsallowcors'])

    @rpc_nsallowcors.setter
    def rpc_nsallowcors(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['rpc']['nsallowcors'] = v

    @property
    def p2p(self):
        return self.__conf['p2p']

    @property
    def p2p_netprotocoladdr(self):
        return str(self.__conf['p2p']['netprotocoladdr'])

    @p2p_netprotocoladdr.setter
    def p2p_netprotocoladdr(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['p2p']['netprotocoladdr'] = v

    @property
    def p2p_netprotocolport(self):
        return int(self.__conf['p2p']['netprotocolport'])

    @p2p_netprotocolport.setter
    def p2p_netprotocolport(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['p2p']['netprotocolport'] = v

    @property
    def p2p_npbindaddr(self):
        return str(self.__conf['p2p']['npbindaddr'])

    @p2p_npbindaddr.setter
    def p2p_npbindaddr(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['p2p']['npbindaddr'] = v

    @property
    def p2p_npbindport(self):
        return int(self.__conf['p2p']['npbindport'])

    @p2p_npbindport.setter
    def p2p_npbindport(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['p2p']['npbindport'] = v

    @property
    def p2p_nptls(self):
        return bool(self.__conf['p2p']['nptls'])

    @p2p_nptls.setter
    def p2p_nptls(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['p2p']['nptls'] = v

    @property
    def p2p_npcert(self):
        return str(self.__conf['p2p']['npcert'])

    @p2p_npcert.setter
    def p2p_npcert(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['p2p']['npcert'] = v

    @property
    def p2p_npkey(self):
        return str(self.__conf['p2p']['npkey'])

    @p2p_npkey.setter
    def p2p_npkey(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['p2p']['npkey'] = v

    @property
    def p2p_npaddpeers(self):
        return self.__conf['p2p']['npaddpeers']

    @p2p_npaddpeers.setter
    def p2p_npaddpeers(self, v):
        if not isinstance(v, list):
            raise TypeError('input value should be an array type')
        self.__conf['p2p']['npaddpeers'] = v

    @property
    def p2p_nphiddenpeers(self):
        return self.__conf['p2p']['nphiddenpeers']

    @p2p_nphiddenpeers.setter
    def p2p_nphiddenpeers(self, v):
        if not isinstance(v, list):
            raise TypeError('input value should be an array type')
        self.__conf['p2p']['nphiddenpeers'] = v

    @property
    def p2p_npdiscoverpeers(self):
        return bool(self.__conf['p2p']['npdiscoverpeers'])

    @p2p_npdiscoverpeers.setter
    def p2p_npdiscoverpeers(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['p2p']['npdiscoverpeers'] = v

    @property
    def p2p_npmaxpeers(self):
        return int(self.__conf['p2p']['npmaxpeers'])

    @p2p_npmaxpeers.setter
    def p2p_npmaxpeers(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['p2p']['npmaxpeers'] = v

    @property
    def p2p_nppeerpool(self):
        return int(self.__conf['p2p']['nppeerpool'])

    @p2p_nppeerpool.setter
    def p2p_nppeerpool(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['p2p']['nppeerpool'] = v

    @property
    def p2p_npexposeself(self):
        return bool(self.__conf['p2p']['npexposeself'])

    @p2p_npexposeself.setter
    def p2p_npexposeself(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['p2p']['npexposeself'] = v

    @property
    def p2p_npusepolaris(self):
        return bool(self.__conf['p2p']['npusepolaris'])

    @p2p_npusepolaris.setter
    def p2p_npusepolaris(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['p2p']['npusepolaris'] = v

    @property
    def p2p_npaddpolarises(self):
        return self.__conf['p2p']['npaddpolarises']

    @p2p_npaddpolarises.setter
    def p2p_npaddpolarises(self, v):
        if not isinstance(v, list):
            raise TypeError('input value should be an array type')
        self.__conf['p2p']['npaddpolarises'] = v

    @property
    def p2p_logfullpeerid(self):
        return bool(self.__conf['p2p']['logfullpeerid'])

    @p2p_logfullpeerid.setter
    def p2p_logfullpeerid(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['p2p']['logfullpeerid'] = v

    @property
    def polaris(self):
        return self.__conf['polaris']

    @property
    def polaris_allowprivate(self):
        return bool(self.__conf['polaris']['allowprivate'])

    @polaris_allowprivate.setter
    def polaris_allowprivate(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['polaris']['allowprivate'] = v

    @property
    def polaris_genesisfile(self):
        return str(self.__conf['polaris']['genesisfile'])

    @polaris_genesisfile.setter
    def polaris_genesisfile(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['polaris']['genesisfile'] = v

    @property
    def blockchain(self):
        return self.__conf['blockchain']

    @property
    def blockchain_maxblocksize(self):
        return int(self.__conf['blockchain']['maxblocksize'])

    @blockchain_maxblocksize.setter
    def blockchain_maxblocksize(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['blockchain']['maxblocksize'] = v

    @property
    def blockchain_coinbaseaccount(self):
        return str(self.__conf['blockchain']['coinbaseaccount'])

    @blockchain_coinbaseaccount.setter
    def blockchain_coinbaseaccount(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['blockchain']['coinbaseaccount'] = v

    @property
    def blockchain_maxanchorcount(self):
        return int(self.__conf['blockchain']['maxanchorcount'])

    @blockchain_maxanchorcount.setter
    def blockchain_maxanchorcount(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['blockchain']['maxanchorcount'] = v

    @property
    def blockchain_verifiercount(self):
        return int(self.__conf['blockchain']['verifiercount'])

    @blockchain_verifiercount.setter
    def blockchain_verifiercount(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['blockchain']['verifiercount'] = v

    @property
    def blockchain_forceresetheight(self):
        return int(self.__conf['blockchain']['forceresetheight'])

    @blockchain_forceresetheight.setter
    def blockchain_forceresetheight(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['blockchain']['forceresetheight'] = v

    @property
    def blockchain_zerofee(self):
        return bool(self.__conf['blockchain']['zerofee'])

    @blockchain_zerofee.setter
    def blockchain_zerofee(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['blockchain']['zerofee'] = v

    @property
    def mempool(self):
        return self.__conf['mempool']

    @property
    def mempool_showmetrics(self):
        return bool(self.__conf['mempool']['showmetrics'])

    @mempool_showmetrics.setter
    def mempool_showmetrics(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['mempool']['showmetrics'] = v

    @property
    def mempool_enablefadeout(self):
        return bool(self.__conf['mempool']['enablefadeout'])

    @mempool_enablefadeout.setter
    def mempool_enablefadeout(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['mempool']['enablefadeout'] = v

    @property
    def mempool_fadeoutperiod(self):
        return int(self.__conf['mempool']['fadeoutperiod'])

    @mempool_fadeoutperiod.setter
    def mempool_fadeoutperiod(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['mempool']['fadeoutperiod'] = v

    @property
    def mempool_verifiers(self):
        return int(self.__conf['mempool']['verifiers'])

    @mempool_verifiers.setter
    def mempool_verifiers(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['mempool']['verifiers'] = v

    @property
    def mempool_dumpfilepath(self):
        return str(self.__conf['mempool']['dumpfilepath'])

    @mempool_dumpfilepath.setter
    def mempool_dumpfilepath(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['mempool']['dumpfilepath'] = v

    @property
    def consensus(self):
        return self.__conf['consensus']

    @property
    def consensus_enablebp(self):
        return bool(self.__conf['consensus']['enablebp'])

    @consensus_enablebp.setter
    def consensus_enablebp(self, v):
        if not isinstance(v, bool):
            raise TypeError('input value should be a boolean type')
        self.__conf['consensus']['enablebp'] = v

    @property
    def consensus_blockinterval(self):
        return int(self.__conf['consensus']['blockinterval'])

    @consensus_blockinterval.setter
    def consensus_blockinterval(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['consensus']['blockinterval'] = v

    @property
    def consensus_raft(self):
        return self.__conf['consensus']['raft']

    @consensus_raft.setter
    def consensus_raft(self, v):
        self.__conf['consensus']['raft'] = v

    @property
    def monitor(self):
        return self.__conf['monitor']

    @property
    def monitor_protocol(self):
        return str(self.__conf['monitor']['protocol'])

    @monitor_protocol.setter
    def monitor_protocol(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['monitor']['protocol'] = v

    @property
    def monitor_endpoint(self):
        return str(self.__conf['monitor']['endpoint'])

    @monitor_endpoint.setter
    def monitor_endpoint(self, v):
        if not isinstance(v, str):
            raise TypeError('input value should be a string type')
        self.__conf['monitor']['endpoint'] = v

    @property
    def account(self):
        return self.__conf['account']

    @property
    def account_unlocktimeout(self):
        return int(self.__conf['account']['unlocktimeout'])

    @account_unlocktimeout.setter
    def account_unlocktimeout(self, v):
        if not isinstance(v, int):
            raise TypeError('input value should be an integer type')
        self.__conf['account']['unlocktimeout'] = v


