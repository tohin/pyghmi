# Copyright 2013 IBM Corp.


payload_types = {
    'ipmi': 0x0,
    'sol' : 0x1,
    'rmcpplusopenreq': 0x10,
    'rmcpplusopenresponse': 0x11,
    'rakp1': 0x12,
    'rakp2': 0x13,
    'rakp3': 0x14,
    'rakp4': 0x15,
}

rmcp_codes = {
    1: 'Insufficient resources to create new session (wait for existing sessions to timeout)',
    2: 'Invalid Session ID',
    3: 'Invalid payload type',
    4: 'Invalid authentication algorithm',
    5: 'Invalid integrity algorithm',
    6: 'No matching integrity payload',
    7: 'No matching integrity payload',
    8: 'Inactive Session ID',
    9: 'Invalid role',
    0xa: 'Unauthorized role or privilege level requested',
    0xb: 'Insufficient resources tocreate a session at the requested role',
    0xc: 'Invalid username length',
    0xd: 'Unauthorized name',
    0xe: 'Unauthorized GUID',
    0xf: 'Invalid integrity check value',
    0x10: 'Invalid confidentiality algorithm',
    0x11: 'No Cipher suite match with proposed security algorithms',
    0x12: 'Illegal or unrecognized parameter',
}

command_completion_codes = {
    (7,0x39): {
        0x81: "Invalid user name",
        0x82: "Null user disabled",
    },
    (7,0x3a): {
        0x81: "No available login slots",
        0x82: "No available login slots for requested user",
        0x83: "No slot available with requested privilege level",
        0x84: "Session sequence number out of range",
        0x85: "Invalid session ID",
        0x86: "Requested privilege level exceeds requested user permissions on this channel",
    },
    (7,0x3b): { #Set session privilege level
        0x80: "User is not allowed requested priveleg level",
        0x81: "Requested privilege level is not allowed over this channel",
        0x82: "Cannot disable user level authentication",
    },
    (1,8): { #set system boot options
        0x80: "Parameter not supported",
        0x81: "Attempt to set set 'set in progress' when not 'set complete'",
        0x82: "Attempt to write read-only parameter",
    }
    
}

ipmi_completion_codes = {
    0x0: "Success",
    0xc0: "Node Busy",
    0xc1: "Invalid command",
    0xc2: "Invalid command for given LUN",
    0xc3: "Timeout while processing command",
    0xc4: "Out of storage space on BMC",
    0xc5: "Reservation canceled or invalid reservation ID",
    0xc6: "Request data truncated",
    0xc7: "Request data length invalid",
    0xc8: "Request data field length limit exceeded",
    0xc9: "Parameter out of range",
    0xca: "Cannot return number of requested data bytes",
    0xcb: "Requested sensor, data, or record not present",
    0xcc: "Invalid data field in request",
    0xcd: "Command illegal for specified sensor or record type",
    0xce: "Command response could not be provided",
    0xcf: "Cannot execute duplicated request",
    0xd0: "SDR repository in update mode",
    0xd1: "Device in firmware update mode",
    0xd2: "BMC initialization in progress",
    0xd3: "Internal destination unavailable",
    0xd4: "Insufficient privilege level or firmware firewall",
    0xd5: "Command not supported in present state",
    0xd6: "Cannot execute command because subfunction disabled or unavailable",
    0xff: "Unspecified",
}

