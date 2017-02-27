#!/usr/bin/python
import  os

def between( i, l, u ):
    if i >= l and i < u:
        return True
    return False

f = open( '/proc/version', 'r' )
tokens = f.readline().strip().split()
f.close()
# DEBUG print tokens
infos = tokens[2].split('-')
series = infos[0]
version = infos[1].split('.')
# DEBUG print "series='%s', version='%s'" % (series, version)
if version[-1].startswith( 'el5' ): version.pop()
if version[-1].startswith( 'amd64' ): version.pop()
if len(version) < 4:
    vendor = "RHEL"
else:
    vendor = "OEL"
# DEBUG print version
rel = int( version[0] )
#
distro = "DUNNO"
errata = "DUNNO"
codename = " (DUNNO)"
#
if series == "2.6.9":
    distro = "4"
    errata = version[0:1]
elif series == '2.6.18':
    distro = "5"
    if between( rel, 8, 53 ):
        errata = "-GA"
        if vendor == "OEL":
            codename = " (Carthage)"
        else:
            codename = " (Tikanga)"
    elif between( rel, 53, 92 ):
        errata = "u1"
        if vendor == "OEL":
            codename = " (Carthage)"
        else:
            codename = " (Tikanga)"
    elif between( rel, 92, 128 ):
        errata = "u2"
        if vendor == "OEL":
            codename = " (Carthage)"
        else:
            codename = " (Tikanga)"
    elif between( rel, 128, 164 ):
        errata = "u3"
        codename = " (Tikanga)"
    elif between( rel, 164, 194 ):
        errata = "u4"
        codename = " (Tikanga)"
    elif between( rel, 194, 999 ):
        errata = "u5"
        codename = " (Tikanga)"
    else:
        errata = "DUNNO"
elif series == '2.6.32':
    distro = "6"
    if between( rel, 0, 999 ):
        errata = "b1"
    else:
        errata = "DUNNO"
    codename = " (FIXME)"
print "%s%s%s%s" % (vendor, distro, errata, codename)
