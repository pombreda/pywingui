# ifdef.py
# Copyright (c) 2012 Maxim Kolosov

NET_IF_OPER_STATUS_DOWN_NOT_AUTHENTICATED = 0x00000001
NET_IF_OPER_STATUS_DOWN_NOT_MEDIA_CONNECTED = 0x00000002
NET_IF_OPER_STATUS_DORMANT_PAUSED = 0x00000004
NET_IF_OPER_STATUS_DORMANT_LOW_POWER = 0x00000008
NET_IF_OID_IF_ALIAS = 0x00000001
NET_IF_OID_COMPARTMENT_ID = 0x00000002
NET_IF_OID_NETWORK_GUID = 0x00000003
NET_IF_OID_IF_ENTRY = 0x00000004
NET_SITEID_UNSPECIFIED = 0
NET_SITEID_MAXUSER = 0x07ffffff
NET_SITEID_MAXSYSTEM = 0x0fffffff
NET_IFINDEX_UNSPECIFIED = 0
NET_IFLUID_UNSPECIFIED = 0
NIIF_HARDWARE_INTERFACE = 0x00000001
NIIF_FILTER_INTERFACE = 0x00000002
NIIF_NDIS_RESERVED1 = 0x00000004
NIIF_NDIS_RESERVED2 = 0x00000008
NIIF_NDIS_RESERVED3 = 0x00000010
NIIF_NDIS_WDM_INTERFACE = 0x00000020
NIIF_NDIS_ENDPOINT_INTERFACE = 0x00000040
IF_MAX_STRING_SIZE = 256
IF_MAX_PHYS_ADDRESS_LENGTH = 32

MIN_IF_TYPE = 1
IF_TYPE_OTHER = 1
IF_TYPE_REGULAR_1822 = 2
IF_TYPE_HDH_1822 = 3
IF_TYPE_DDN_X25 = 4
IF_TYPE_RFC877_X25 = 5
IF_TYPE_ETHERNET_CSMACD = 6
IF_TYPE_IS088023_CSMACD = 7
IF_TYPE_ISO88024_TOKENBUS = 8
IF_TYPE_ISO88025_TOKENRING = 9
IF_TYPE_ISO88026_MAN = 10
IF_TYPE_STARLAN = 11
IF_TYPE_PROTEON_10MBIT = 12
IF_TYPE_PROTEON_80MBIT = 13
IF_TYPE_HYPERCHANNEL = 14
IF_TYPE_FDDI = 15
IF_TYPE_LAP_B = 16
IF_TYPE_SDLC = 17
IF_TYPE_DS1 = 18
IF_TYPE_E1 = 19
IF_TYPE_BASIC_ISDN = 20
IF_TYPE_PRIMARY_ISDN = 21
IF_TYPE_PROP_POINT2POINT_SERIAL = 22
IF_TYPE_PPP = 23
IF_TYPE_SOFTWARE_LOOPBACK = 24
IF_TYPE_EON = 25
IF_TYPE_ETHERNET_3MBIT = 26
IF_TYPE_NSIP = 27
IF_TYPE_SLIP = 28
IF_TYPE_ULTRA = 29
IF_TYPE_DS3 = 30
IF_TYPE_SIP = 31
IF_TYPE_FRAMERELAY = 32
IF_TYPE_RS232 = 33
IF_TYPE_PARA = 34
IF_TYPE_ARCNET = 35
IF_TYPE_ARCNET_PLUS = 36
IF_TYPE_ATM = 37
IF_TYPE_MIO_X25 = 38
IF_TYPE_SONET = 39
IF_TYPE_X25_PLE = 40
IF_TYPE_ISO88022_LLC = 41
IF_TYPE_LOCALTALK = 42
IF_TYPE_SMDS_DXI = 43
IF_TYPE_FRAMERELAY_SERVICE = 44
IF_TYPE_V35 = 45
IF_TYPE_HSSI = 46
IF_TYPE_HIPPI = 47
IF_TYPE_MODEM = 48
IF_TYPE_AAL5 = 49
IF_TYPE_SONET_PATH = 50
IF_TYPE_SONET_VT = 51
IF_TYPE_SMDS_ICIP = 52
IF_TYPE_PROP_VIRTUAL = 53
IF_TYPE_PROP_MULTIPLEXOR = 54
IF_TYPE_IEEE80212 = 55
IF_TYPE_FIBRECHANNEL = 56
IF_TYPE_HIPPIINTERFACE = 57
IF_TYPE_FRAMERELAY_INTERCONNECT = 58
IF_TYPE_AFLANE_8023 = 59
IF_TYPE_AFLANE_8025 = 60
IF_TYPE_CCTEMUL = 61
IF_TYPE_FASTETHER = 62
IF_TYPE_ISDN = 63
IF_TYPE_V11 = 64
IF_TYPE_V36 = 65
IF_TYPE_G703_64K = 66
IF_TYPE_G703_2MB = 67
IF_TYPE_QLLC = 68
IF_TYPE_FASTETHER_FX = 69
IF_TYPE_CHANNEL = 70
IF_TYPE_IEEE80211 = 71
IF_TYPE_IBM370PARCHAN = 72
IF_TYPE_ESCON = 73
IF_TYPE_DLSW = 74
IF_TYPE_ISDN_S = 75
IF_TYPE_ISDN_U = 76
IF_TYPE_LAP_D = 77
IF_TYPE_IPSWITCH = 78
IF_TYPE_RSRB = 79
IF_TYPE_ATM_LOGICAL = 80
IF_TYPE_DS0 = 81
IF_TYPE_DS0_BUNDLE = 82
IF_TYPE_BSC = 83
IF_TYPE_ASYNC = 84
IF_TYPE_CNR = 85
IF_TYPE_ISO88025R_DTR = 86
IF_TYPE_EPLRS = 87
IF_TYPE_ARAP = 88
IF_TYPE_PROP_CNLS = 89
IF_TYPE_HOSTPAD = 90
IF_TYPE_TERMPAD = 91
IF_TYPE_FRAMERELAY_MPI = 92
IF_TYPE_X213 = 93
IF_TYPE_ADSL = 94
IF_TYPE_RADSL = 95
IF_TYPE_SDSL = 96
IF_TYPE_VDSL = 97
IF_TYPE_ISO88025_CRFPRINT = 98
IF_TYPE_MYRINET = 99
IF_TYPE_VOICE_EM = 100
IF_TYPE_VOICE_FXO = 101
IF_TYPE_VOICE_FXS = 102
IF_TYPE_VOICE_ENCAP = 103
IF_TYPE_VOICE_OVERIP = 104
IF_TYPE_ATM_DXI = 105
IF_TYPE_ATM_FUNI = 106
IF_TYPE_ATM_IMA = 107
IF_TYPE_PPPMULTILINKBUNDLE = 108
IF_TYPE_IPOVER_CDLC = 109
IF_TYPE_IPOVER_CLAW = 110
IF_TYPE_STACKTOSTACK = 111
IF_TYPE_VIRTUALIPADDRESS = 112
IF_TYPE_MPC = 113
IF_TYPE_IPOVER_ATM = 114
IF_TYPE_ISO88025_FIBER = 115
IF_TYPE_TDLC = 116
IF_TYPE_GIGABITETHERNET = 117
IF_TYPE_HDLC = 118
IF_TYPE_LAP_F = 119
IF_TYPE_V37 = 120
IF_TYPE_X25_MLP = 121
IF_TYPE_X25_HUNTGROUP = 122
IF_TYPE_TRANSPHDLC = 123
IF_TYPE_INTERLEAVE = 124
IF_TYPE_FAST = 125
IF_TYPE_IP = 126
IF_TYPE_DOCSCABLE_MACLAYER = 127
IF_TYPE_DOCSCABLE_DOWNSTREAM = 128
IF_TYPE_DOCSCABLE_UPSTREAM = 129
IF_TYPE_A12MPPSWITCH = 130
IF_TYPE_TUNNEL = 131
IF_TYPE_COFFEE = 132
IF_TYPE_CES = 133
IF_TYPE_ATM_SUBINTERFACE = 134
IF_TYPE_L2_VLAN = 135
IF_TYPE_L3_IPVLAN = 136
IF_TYPE_L3_IPXVLAN = 137
IF_TYPE_DIGITALPOWERLINE = 138
IF_TYPE_MEDIAMAILOVERIP = 139
IF_TYPE_DTM = 140
IF_TYPE_DCN = 141
IF_TYPE_IPFORWARD = 142
IF_TYPE_MSDSL = 143
IF_TYPE_IEEE1394 = 144
IF_TYPE_IF_GSN = 145
IF_TYPE_DVBRCC_MACLAYER = 146
IF_TYPE_DVBRCC_DOWNSTREAM = 147
IF_TYPE_DVBRCC_UPSTREAM = 148
IF_TYPE_ATM_VIRTUAL = 149
IF_TYPE_MPLS_TUNNEL = 150
IF_TYPE_SRP = 151
IF_TYPE_VOICEOVERATM = 152
IF_TYPE_VOICEOVERFRAMERELAY = 153
IF_TYPE_IDSL = 154
IF_TYPE_COMPOSITELINK = 155
IF_TYPE_SS7_SIGLINK = 156
IF_TYPE_PROP_WIRELESS_P2P = 157
IF_TYPE_FR_FORWARD = 158
IF_TYPE_RFC1483 = 159
IF_TYPE_USB = 160
IF_TYPE_IEEE8023AD_LAG = 161
IF_TYPE_BGP_POLICY_ACCOUNTING = 162
IF_TYPE_FRF16_MFR_BUNDLE = 163
IF_TYPE_H323_GATEKEEPER = 164
IF_TYPE_H323_PROXY = 165
IF_TYPE_MPLS = 166
IF_TYPE_MF_SIGLINK = 167
IF_TYPE_HDSL2 = 168
IF_TYPE_SHDSL = 169
IF_TYPE_DS1_FDL = 170
IF_TYPE_POS = 171
IF_TYPE_DVB_ASI_IN = 172
IF_TYPE_DVB_ASI_OUT = 173
IF_TYPE_PLC = 174
IF_TYPE_NFAS = 175
IF_TYPE_TR008 = 176
IF_TYPE_GR303_RDT = 177
IF_TYPE_GR303_IDT = 178
IF_TYPE_ISUP = 179
IF_TYPE_PROP_DOCS_WIRELESS_MACLAYER = 180
IF_TYPE_PROP_DOCS_WIRELESS_DOWNSTREAM = 181
IF_TYPE_PROP_DOCS_WIRELESS_UPSTREAM = 182
IF_TYPE_HIPERLAN2 = 183
IF_TYPE_PROP_BWA_P2MP = 184
IF_TYPE_SONET_OVERHEAD_CHANNEL = 185
IF_TYPE_DIGITAL_WRAPPER_OVERHEAD_CHANNEL = 186
IF_TYPE_AAL2 = 187
IF_TYPE_RADIO_MAC = 188
IF_TYPE_ATM_RADIO = 189
IF_TYPE_IMT = 190
IF_TYPE_MVL = 191
IF_TYPE_REACH_DSL = 192
IF_TYPE_FR_DLCI_ENDPT = 193
IF_TYPE_ATM_VCI_ENDPT = 194
IF_TYPE_OPTICAL_CHANNEL = 195
IF_TYPE_OPTICAL_TRANSPORT = 196
MAX_IF_TYPE = 196
IF_CHECK_NONE = 0x00
IF_CHECK_MCAST = 0x01
IF_CHECK_SEND = 0x02
IF_CONNECTION_DEDICATED = 1
IF_CONNECTION_PASSIVE = 2
IF_CONNECTION_DEMAND = 3
IF_ADMIN_STATUS_UP = 1
IF_ADMIN_STATUS_DOWN = 2
IF_ADMIN_STATUS_TESTING = 3
MIB_IF_TYPE_OTHER = 1
MIB_IF_TYPE_ETHERNET = 6
MIB_IF_TYPE_TOKENRING = 9
MIB_IF_TYPE_FDDI = 15
MIB_IF_TYPE_PPP = 23
MIB_IF_TYPE_LOOPBACK = 24
MIB_IF_TYPE_SLIP = 28
MIB_IF_ADMIN_STATUS_UP = 1
MIB_IF_ADMIN_STATUS_DOWN = 2
MIB_IF_ADMIN_STATUS_TESTING = 3

from ctypes import *

class INFO(Structure):
	'bit field types other than int'
	_fields_ = [('Reserved', c_ulonglong, 24),
	('NetLuidIndex', c_ulonglong, 24),
	('IfType', c_ulonglong, 16)]# equal to IANA IF type
class NET_LUID_LH(Union):
	_fields_ = [('Value', c_ulonglong), ('Info', INFO)]
PNET_LUID_LH = POINTER(NET_LUID_LH)

IF_LUID = NET_LUID = NET_LUID_LH
PIF_LUID = PNET_LUID_LH
