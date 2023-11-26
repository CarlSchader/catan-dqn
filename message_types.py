# all message types, for server client communication.
codes_to_types = {
    999: 'AUTHREQUEST',
    1000: 'NULLMESSAGE',
    1001: 'NEWCHANNEL',
    1002: 'CHANNELMEMBERS',
    1003: 'CHANNELS',
    1004: 'JOINCHANNEL',
    1005: 'CHANNELTEXTMSG',
    1006: 'LEAVECHANNEL',
    1007: 'DELETECHANNEL',
    1008: 'LEAVEALL',
    1009: 'PUTPIECE',
    1010: 'GAMETEXTMSG',
    1011: 'LEAVEGAME',
    1012: 'SITDOWN',
    1013: 'JOINGAME',
    1014: 'BOARDLAYOUT',
    1015: 'DELETEGAME',
    1016: 'NEWGAME',
    1017: 'GAMEMEMBERS',
    1018: 'STARTGAME',
    1019: 'GAMES',
    1020: 'JOINCHANNELAUTH',
    1021: 'JOINGAMEAUTH',
    1022: 'IMAROBOT',
    1023: 'BOTJOINGAMEREQUEST',
    1024: 'PLAYERELEMENT',
    1025: 'GAMESTATE',
    1026: 'TURN',
    1028: 'DICERESULT',
    1029: 'DISCARDREQUEST',
    1030: 'ROLLDICEREQUEST',
    1031: 'ROLLDICE',
    1032: 'ENDTURN',
    1033: 'DISCARD',
    1034: 'MOVEROBBER',
    1035: 'CHOOSEPLAYER',
    1036: 'CHOOSEPLAYERREQUEST',
    1037: 'REJECTOFFER',
    1038: 'CLEAROFFER',
    1039: 'ACCEPTOFFER',
    1040: 'BANKTRADE',
    1041: 'MAKEOFFER',
    1042: 'CLEARTRADEMSG',
    1043: 'BUILDREQUEST',
    1044: 'CANCELBUILDREQUEST',
    1045: 'BUYDEVCARDREQUEST',
    1046: 'DEVCARDACTION',
    1047: 'DEVCARDCOUNT',
    1048: 'SETPLAYEDDEVCARD',
    1049: 'PLAYDEVCARDREQUEST',
    1052: 'PICKRESOURCES',
    1053: 'PICKRESOURCETYPE',
    1054: 'FIRSTPLAYER',
    1055: 'SETTURN',
    1056: 'ROBOTDISMISS',
    1057: 'POTENTIALSETTLEMENTS',
    1058: 'CHANGEFACE',
    1059: 'REJECTCONNECTION',
    1060: 'LASTSETTLEMENT',
    1061: 'GAMESTATS',
    1062: 'BCASTTEXTMSG',
    1063: 'RESOURCECOUNT',
    1064: 'ADMINPING',
    1065: 'ADMINRESET',
    1066: 'LONGESTROAD',
    1067: 'LARGESTARMY',
    1068: 'SETSEATLOCK',
    1069: 'STATUSMESSAGE',
    1070: 'CREATEACCOUNT',
    1071: 'UPDATEROBOTPARAMS',
    1072: 'ROLLDICEPROMPT',
    1073: 'RESETBOARDREQUEST',
    1074: 'RESETBOARDAUTH',
    1075: 'RESETBOARDVOTEREQUEST',
    1076: 'RESETBOARDVOTE',
    1077: 'RESETBOARDREJECT',
    1078: 'NEWGAMEWITHOPTIONSREQUEST',
    1079: 'NEWGAMEWITHOPTIONS',
    1080: 'GAMEOPTIONGETDEFAULTS',
    1081: 'GAMEOPTIONGETINFOS',
    1082: 'GAMEOPTIONINFO',
    1083: 'GAMESWITHOPTIONS',
    1084: 'BOARDLAYOUT2',
    1085: 'PLAYERSTATS',
    1086: 'PLAYERELEMENTS',
    1087: 'DEBUGFREEPLACE',
    1088: 'TIMINGPING',
    1089: 'SIMPLEREQUEST',
    1090: 'SIMPLEACTION',
    1091: 'GAMESERVERTEXT',
    1092: 'DICERESULTRESOURCES',
    1093: 'MOVEPIECE',
    1094: 'REMOVEPIECE',
    1095: 'PIECEVALUE',
    1096: 'GAMEELEMENTS',
    1097: 'SVPTEXTMSG',
    1098: 'INVENTORYITEMACTION',
    1099: 'SETSPECIALITEM',
    1100: 'LOCALIZEDSTRINGS',
    1101: 'SCENARIOINFO',
    1102: 'ROBBERYRESULT',
    1103: 'BOTGAMEDATACHECK',
    1104: 'DECLINEPLAYERREQUEST',
    1105: 'UNDOPUTPIECE',
    1106: 'SETLASTACTION',
    9998: 'VERSION',
    9999: 'SERVERPING',
    100001: 'REVEALFOGHEX',
    100002: 'SETSHIPROUTECLOSED',
}

types_to_codes = {v: k for k, v in codes_to_types.items()}

# Token separators. At most one SEP per message; multiple SEP2 are allowed after SEP.
#      * For multi-messages, multiple SEP are allowed;
SEP = '|'

# separator, in regexp form for splits and replacements.
SEP_RE = '\\|'

SEP2 = ','

def interpret_server_message(msg):
    sub_msgs = msg.split(SEP)
    sub_msgs = [sub_msg.replace('\x00', '').replace('\x05', '').strip() for sub_msg in sub_msgs]
    
    for i in range(len(sub_msgs)):
        sub_msg = sub_msgs[i]
        if sub_msg.isdigit() and int(sub_msg) in codes_to_types:
            sub_msgs[i] = codes_to_types[int(sub_msg)]

    return sub_msgs

def format_client_message(msg):
    splits = msg.split(SEP)
    for i in range(len(splits)):
        s = splits[i]
        if s in types_to_codes:
            splits[i] = str(types_to_codes[s])
    return SEP.join(splits)