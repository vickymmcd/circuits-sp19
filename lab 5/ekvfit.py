import tkplot, math
from numpy import *

def num2str(x, n = 0):
#    if not ((type(x) is float) or (type(x) is int) or (type(x) is long)):
#        raise TypeError('x must be a numeric data type')
    x = float(x)
    multipliers = (1., 1e-3, 1e-6, 1e-9, 1e-12, 1e-15, 1e-18, 1e-21, 1e-24, 
                   1e24, 1e21, 1e18, 1e15, 1e12, 1e9, 1e6, 1e3)
    prefixes = ('', 'k', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y', 
                'y', 'z', 'a', 'f', 'p', 'n', 'u', 'm')
    if abs(x) == 0.:
        index = 0
    else:
        index = int(math.floor(math.log10(abs(x)) / 3.))
    if (index >= -8) and (index <= 8):
        return str(multipliers[index] * x if n == 0 else round(multipliers[index] * x, n)) + prefixes[index]
    else:
        return str(x if n == 0 else round(x, n))

def str2num(s):
#    if not (type(s) is str):
#        raise TypeError('s must be a string')
    multipliers = {'k': 1e3, 'M': 1e6, 'G': 1e9, 'T': 1e12, 'P': 1e15, 'E': 1e18, 'Z': 1e21, 'Y': 1e24, 
                   'y': 1e-24, 'z': 1e-21, 'a': 1e-18, 'f': 1e-15, 'p': 1e-12, 'n': 1e-9, 'u': 1e-6, 'm': 1e-3}
    if s[-1] in multipliers.keys():
        return float(s[0 : -1]) * multipliers[s[-1]]
    else:
        return float(s)

def ekvfit(Vg, Isat, epsilon = 0.001, **kwargs):
    '''
    EKVFIT Attempts to fit a simplified EKV model to (VG, ISAT) pairs.
    EKVFIT(VG, ISAT, EPSILON) attempts to fit a simplified EKV model for
    the saturation region of MOS transistor operation to measured values
    of gate voltage (specified in VG) and channel current (specified in
    ISAT).  The assumed form of the model is

        ISAT = Is * (log(1 + exp(kappa*(VG - VT)/(2*0.0258)))).^2

    The return values are [Is, VT, kappa].  EKVFIT makes use of LINEFIT.
    First, it attempts to find parameters for the weak-inversion region by
    using LINEFIT on VG and log(ISAT).  Then, it attepts to find
    parameters for the strong-inversion region by using LINEFIT on VG and
    sqrt(ISAT).  It then uses the x-axis intercept from the
    strong-inversion fit as a starting value for VT and computes a
    starting value for IS via cubic-spline interpolation as twice the
    value of ISAT when VG = VT.  EKVFIT then attepts to find a the value
    of IS in the interval between one tenth the initial value of IS and
    ten times the inital value of IS that minimizes the curvature of the
    inverse EKV model applied to ISAT, given by

                     log(exp(sqrt(ISAT/Is)) - 1),

    when plotted as a function of VG, using the golden-section search.
    Once the best value of Is is found, EKVFIT uses LINEFIT to get the
    slope and intercept of the best-fit line to the EKV model inverse
    expression, given above, applied to ISAT versus VG.  The slope of this
    curve should be kappa/(2*UT) and the VG-axis intercept should be VT.

    See the LINEFIT docstring for an explanation of the EPSILON 
    parameter.
    '''
    if not isinstance(Vg, ndarray) or not isinstance(Isat, ndarray):
        raise TypeError('Vg and Isat must both be ndarrays')
    if len(Vg) != len(Isat):
        raise IndexError('Vg and Isat must have the same length')
    plotting = kwargs.get('plotting', 'off')
    if plotting not in ('on', 'off'):
        raise ValueError("if supplied, plotting must be either 'on' or 'off'")
    if plotting == 'on':
        fig = tkplot.tkplot()

    Is = 0
    VT = 0
    kappa = 0

    [WIfirst, WIlast, WIm, WIb, WIN] = linefit(Vg, log(Isat), epsilon)
    if WIN == 0:
        raise RuntimeError('could not find a weak-inversion region')
    elif plotting == 'on':
        fig.semilogy(Vg, Isat)
        temp = fig.ylimits()
        fig.semilogy([Vg, array(Vg[WIfirst : WIlast + 1]), Vg], [Isat, array(Isat[WIfirst : WIlast + 1]), exp(WIm * Vg + WIb)], ['b.', 'r.', 'k-'])
        fig.ylimits(temp)
        fig.xlabel('VG (V)')
        fig.ylabel('Isat (A)')
        fig.ylabel('Weak-Inversion Fit', side = 'right')
        raw_input()
    if min(abs(array(Isat[WIfirst : WIlast + 1]))) > 1e-6:
        raise ValueError('identified a candidate weak-inversion region, but all current levels exceed typical weak-inversion currents')
    if max(abs(array(Isat[WIfirst : WIlast + 1]))) > 1e-6:
        print 'ValueWarning: identified a candidate weak-inversion region, but some current levels exceed typical weak-inversion currents'
#        warnings.warn('ValueWarning', 'identified a candidate weak-inversion region, but some current levels exceed typical weak-inversion currents')

    [SIfirst, SIlast, SIm, SIb, SIN] = linefit(Vg, sqrt(Isat), epsilon)
    if SIN == 0:
        raise RuntimeError('could not find a strong-inversion region')
    elif plotting == 'on':
        fig.plot(Vg, sqrt(abs(Isat)))
        temp = fig.ylimits()
        fig.plot([Vg, array(Vg[SIfirst : SIlast+1]), Vg], [sqrt(abs(Isat)), sqrt(array(Isat[SIfirst : SIlast + 1])), SIm * Vg + SIb], ['b.', 'r.', 'k-'])
        fig.ylimits(temp)
        fig.xlabel('VG (V)')
        fig.ylabel('sqrt(Isat) (sqrt(A))')
        fig.ylabel('Strong-Inversion Fit', side = 'right')
        raw_input()
    if max(abs(array(Isat[SIfirst : SIlast + 1]))) < 0.1e-6:
        raise ValueError('identified a candidate strong-inversion region, but all current levels are lower than typical strong-inversion currents')
    if min(abs(array(Isat[SIfirst : SIlast + 1]))) < 0.1e-6:
        print 'ValueWarning: identified a candidate strong-inversion region, but some current levels are lower than typical strong-inversion currents'
#        warnings.warn('ValueWarning', 'identified a candidate strong-inversion region, but some current levels are lower than typical strong-inversion currents')

    if SIfirst > WIlast:
        first = WIfirst
        last = SIlast
    elif WIfirst > SIlast:
        first = SIfirst
        last = WIlast
    else:
        raise RuntimeError('weak-inversion and strong-inversion regions found were not disjoint');

    VT = -SIb / SIm
#    Is = 2*spline(array(Vg[first:last+1]), array(Isat[first:last+1]), VT)
    for i in range(first, last):
        if ((Vg[i] <= VT) and (Vg[i + 1] > VT)) or ((Vg[i + 1] <= VT) and (Vg[i] > VT)):
            Is = 2 * (Isat[i] + (Isat[i + 1] - Isat[i]) * (VT - Vg[i]) / (Vg[i + 1] - Vg[i]))
            break

    R = 0.61803399
    C = 1. - R
    tol = 1e-4

    x0 = 0.1 * Is
    x1 = Is
    x2 = (1. + 9. * C) * Is
    x3 = 10. * Is

    dVg = diff(array(Vg[first : last + 1]))
    temp = diff(log(exp(sqrt(array(Isat[first : last + 1]) / x1)) - 1)) / dVg
    f1 = std(temp) / mean(temp)
    temp = diff(log(exp(sqrt(array(Isat[first : last + 1]) / x2)) - 1)) / dVg
    f2 = std(temp) / mean(temp)

    while abs(x3 - x0) > tol * (abs(x1) + abs(x2)):
        if f2 < f1:
            x0 = x1
            x1 = x2
            x2 = R * x1 + C * x3
            f1 = f2
            temp = diff(log(exp(sqrt(array(Isat[first : last + 1]) / x2)) - 1)) / dVg
            f2 = std(temp) / mean(temp)
            if plotting == 'on':
                [EKVfirst, EKVlast, m, b, N] = linefit(array(Vg[first : last + 1]), log(exp(sqrt(array(Isat[first : last + 1]) / x2)) - 1), epsilon)
                fig.plot([array(Vg[first:last+1]), array(Vg[first:last+1])], [log(exp(sqrt(array(Isat[first : last + 1]) / x2)) - 1), m * array(Vg[first : last + 1]) + b], ['b.',  'k-'])
                fig.xlabel('VG (V)')
                fig.ylabel('log(exp(sqrt(Isat/Is))-1)')
                fig.ylabel('Optimizing Is = {0}A'.format(num2str(x2, 3)), side = 'right')
                raw_input()
        else:
            x3 = x2
            x2 = x1
            x1 = R * x2 + C * x0
            f2 = f1
            temp = diff(log(exp(sqrt(array(Isat[first : last + 1]) / x1)) - 1)) / dVg
            f1 = std(temp) / mean(temp)
            if plotting == 'on':
                [EKVfirst, EKVlast, m, b, N] = linefit(array(Vg[first : last + 1]), log(exp(sqrt(array(Isat[first : last + 1]) / x1)) - 1), epsilon)
                fig.plot([array(Vg[first : last + 1]), array(Vg[first : last + 1])], [log(exp(sqrt(array(Isat[first : last + 1]) / x1)) - 1), m * array(Vg[first : last + 1]) + b], ['b.',  'k-'])
                fig.xlabel('VG (V)')
                fig.ylabel('log(exp(sqrt(Isat/Is))-1)')
                fig.ylabel('Optimizing Is = {0}A'.format(num2str(x1, 3)), side = 'right')
                raw_input()

    Is = x1 if f1 < f2 else x2

    [EKVfirst, EKVlast, m, b, N] = linefit(array(Vg[first : last + 1]), log(exp(sqrt(array(Isat[first : last + 1]) / Is)) - 1), epsilon)
    VT = -b / m
    kappa = 2 * m *0.0258
    if plotting == 'on':
        fig.semilogy(Vg, Isat)
        temp = fig.ylimits()
        fig.semilogy([Vg, array(Vg[first : last + 1]), Vg], [Isat, array(Isat[first : last + 1]), Is * (log(1 + exp(kappa * (Vg - VT) / (2 * 0.0258)))) ** 2], ['b.', 'r.',  'k-'])
        fig.ylimits(temp)
        fig.xlabel('VG (V)')
        fig.ylabel('Isat (A)')
        fig.ylabel('EKV Fit: Is = {0}A, VT = {1!s}V, kappa = {2!s}'.format(num2str(Is, 3), round(VT, 3), round(kappa, 3)), side = 'right')
        raw_input()
        fig.plot(Vg, sqrt(abs(Isat)))
        temp = fig.ylimits()
        fig.plot([Vg, array(Vg[first : last + 1]), Vg], [sqrt(abs(Isat)), sqrt(array(Isat[first : last + 1])), sqrt(Is * (log(1 + exp(kappa * (Vg - VT) / (2 * 0.0258)))) ** 2)], ['b.', 'r.', 'k-'])
        fig.ylimits(temp)
        fig.xlabel('VG (V)')
        fig.ylabel('sqrt(Isat) (sqrt(A))')
        fig.ylabel('EKV Fit: Is = {0!s}A, VT = {1!s}V, kappa = {2!s}'.format(num2str(Is, 3), round(VT, 3), round(kappa, 3)), side = 'right')
        raw_input()
    return [Is, VT, kappa]

