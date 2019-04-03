#
## Copyright (c) 2018, Bradley A. Minch
## All rights reserved.
##
## Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are met: 
## 
##     1. Redistributions of source code must retain the above copyright 
##        notice, this list of conditions and the following disclaimer. 
##     2. Redistributions in binary form must reproduce the above copyright 
##        notice, this list of conditions and the following disclaimer in the 
##        documentation and/or other materials provided with the distribution. 
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
## AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
## IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
## ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE 
## LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
## CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
## SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
## INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
## CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
## ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
## POSSIBILITY OF SUCH DAMAGE.
#

import Tkinter as tk
import numpy as np
import math
import codecs

class tkplot:

    class curve:

        def __init__(self, **kwargs):
            self.data_x = kwargs.get('data_x', np.array([]))
            self.data_y = kwargs.get('data_y', np.array([]))
            self.points_x = kwargs.get('points_x', [np.array([])])
            self.points_y = kwargs.get('points_y', [np.array([])])
            self.name = kwargs.get('name', '')
            self.yaxis = kwargs.get('yaxis', 'left')
            self.marker_color = kwargs.get('marker_color', '')
            self.marker = kwargs.get('marker', '')
            self.curve_color = kwargs.get('curve_color', '')
            self.curve_style = kwargs.get('curve_style', '')

    class y_axis:

        def __init__(self, **kwargs):
            self.name = kwargs.get('name', 'left')
            self.color = kwargs.get('color', '#000000')
            self.yaxis_mode = kwargs.get('yaxis_mode', 'linear')
            self.yaxis_sign = 1.
            self.ylimits_mode = kwargs.get('ylimits_mode', 'auto')
            self.ylim = kwargs.get('ylim', [0., 1.])
            self.ymin = self.ylim[0]
            self.ymax = self.ylim[1]
            self.ylabel_value = kwargs.get('ylabel', '')

    def __init__(self, **kwargs):
        self.canvas_left = float(kwargs.get('left', 0.))
        self.canvas_top = float(kwargs.get('top', 0.))
        self.canvas_width = float(kwargs.get('width', 560.))
        self.canvas_height = float(kwargs.get('height', 420.))
        self.marker_radius = float(kwargs.get('marker_radius', 4.))
        self.marker_lineweight = float(kwargs.get('marker_lineweight', 1.))
        self.curve_lineweight = float(kwargs.get('curve_lineweight', 1.))
        self.tick_length = float(kwargs.get('tick_length', 6.))
        self.tick_lineweight = float(kwargs.get('tick_lineweight', 1.))
        self.canvas_background_color = kwargs.get('background', '#CDCDCD')
        self.axes_background_color = kwargs.get('axes_background', '#FFFFFF')
        self.axes_color = kwargs.get('axes_color', '#000000')
        self.axes_lineweight = kwargs.get('axes_lineweight', 1.)
        self.label_font_baseline = float(kwargs.get('baseline', 0.6))
        self.label_fontsize = int(kwargs.get('fontsize', 12))
        self.label_font = kwargs.get('font', 'Helvetica')

        self.init_markers(self.marker_radius)

        self.marker_names = [[' ',  'No marker'], ['.', 'Point'], ['o', 'Circle'], ['x', 'Ex'], 
                             ['+', 'Plus'], ['*', 'Star'], ['s', 'Square'], ['d', 'Diamond'],
                             ['v', 'Triangle (down)'], ['^', 'Triangle (up)'], ['<', 'Triangle (left)'], 
                             ['>', 'Triangle (right)'], ['p', 'Pentagram'], ['h', 'Hexagram']]

        self.colors = {'b': '#0000FF', 'g': '#00FF00', 'r': '#FF0000', 
                       'c': '#00FFFF', 'm': '#FF00FF', 'y': '#FFFF00',
                       'k': '#000000', 'w': '#FFFFFF'}

        self.color_names = [['b', 'Blue'], ['r', 'Red'], ['g', 'Green'], ['c', 'Cyan'], 
                            ['m', 'Magenta'], ['y', 'Yellow'], ['k', 'Black'], ['w', 'White']]

        self.linestyles = {'-': (), ':': (1, 4), '--': (10, 4), '-.': (10, 4, 1, 4), '-:': (10, 4, 1, 4, 1, 4)}

        self.linestyle_names = [[' ',   'No line'], ['-',  'Solid'], [':',  'Dotted'], 
                                ['-.', 'Dash-dot'], ['-:', 'Dash-dot-dot'], ['--', 'Dashed']]

        self.multipliers = (1., 1e-3, 1e-6, 1e-9, 1e-12, 1e-15, 1e-18, 1e-21, 1e-24, 
                            1e24, 1e21, 1e18, 1e15, 1e12, 1e9, 1e6, 1e3)

        self.prefixes = (u'', u'k', u'M', u'G', u'T', u'P', u'E', u'Z', u'Y', 
                         u'y', u'z', u'a', u'f', u'p', u'n', u'\xB5', u'm')

        self.default_color_order = ('b', 'g', 'r', 'c', 'm', 'y')
        self.default_color_index = 0
        self.default_marker = '.'
        self.default_curve_style = '-'

        self.curve_id = 0
        self.curves = {}

        self.xaxis_mode = 'linear'
        self.xaxis_sign = 1.
        self.xlimits_mode = 'auto'
        self.xlim = [0., 1.]
        self.xmin = 0.
        self.xmax = 1.
        self.xlabel_value = ''

        self.yaxes = {}
        self.yaxes['left'] = self.y_axis()
        self.left_yaxis = 'left'
        self.right_yaxis = ''

        self.update_sizes()

        self.find_x_ticks()
        self.find_y_ticks()

        self.grid_state = 'off'

        self.dw = 0.
        self.dh = 0.

        self.x0 = 0.
        self.y0 = 0.

        self.svg_file = None
        self.svg_indent_level = 1

        self.tk_backend()

        self.root = kwargs.get('parent')
        if self.root == None:
            self.root = tk.Tk()
            self.root.title('tkplot')
        self.canvas = tk.Canvas(self.root, width = self.canvas_width, height = self.canvas_height, background = self.canvas_background_color, highlightbackground = self.canvas_background_color)

        self.draw_background()
        self.draw_axes()
        self.draw_x_ticks()
        self.draw_y_ticks()
        self.draw_axis_labels()

        self.canvas.pack(fill = 'both', expand = 'yes')
        self.dw = 2.*float(self.canvas.cget('highlightthickness'))
        self.dh = self.dw
        self.canvas.bind('<Configure>', self.resize)

    def init_markers(self, r = 4.):
        r_over_sqrt2 = r / math.sqrt(2.)
        r_over_sqrt3 = r / math.sqrt(3.)
        pi_over_180 = math.pi / 180.
        r2 = r * math.sin(pi_over_180 * 18.) / math.sin(pi_over_180 * 54.)

        self.marker_coords = {}
        self.marker_coords['.'] = ((-0.5 * r, -0.5 * r), (0.5 * r, 0.5 * r))
        self.marker_coords['o'] = ((-r, -r), (r, r))
        self.marker_coords['x'] = ((0., 0.), (r_over_sqrt2, -r_over_sqrt2), 
                                   (0., 0.), (r_over_sqrt2, r_over_sqrt2), 
                                   (0., 0.), (-r_over_sqrt2, r_over_sqrt2), 
                                   (0., 0.), (-r_over_sqrt2, -r_over_sqrt2), 
                                   (0., 0.))
        self.marker_coords['+'] = ((0., 0.), (0., -r), 
                                   (0., 0.), (r, 0.), 
                                   (0., 0.), (0., r), 
                                   (0., 0.), (-r, 0.), 
                                   (0., 0.))
        self.marker_coords['*'] = ((0., 0.), (0., -r), 
                                   (0., 0.), (r_over_sqrt2, -r_over_sqrt2), 
                                   (0., 0.), (r, 0.), 
                                   (0., 0.), (r_over_sqrt2, r_over_sqrt2), 
                                   (0., 0.), (0., r), 
                                   (0., 0.), (-r_over_sqrt2, r_over_sqrt2), 
                                   (0., 0.), (-r, 0.), 
                                   (0., 0.), (-r_over_sqrt2, -r_over_sqrt2), 
                                   (0., 0.))
        self.marker_coords['s'] = ((-r_over_sqrt2, -r_over_sqrt2), (r_over_sqrt2, -r_over_sqrt2), 
                                   (r_over_sqrt2, r_over_sqrt2), (-r_over_sqrt2, r_over_sqrt2), 
                                   (-r_over_sqrt2, -r_over_sqrt2))
        self.marker_coords['d'] = ((0., -1.25 * r), (r, 0.), (0., 1.25 * r), (-r, 0.), (0., -1.25 * r))
        self.marker_coords['v'] = ((0., r), 
                                   (r * math.cos(pi_over_180 * 150.), -r * math.sin(pi_over_180 * 150.)), 
                                   (r * math.cos(pi_over_180 * 30.), -r * math.sin(pi_over_180 * 30.)), 
                                   (0., r))
        self.marker_coords['^'] = ((0., -r), 
                                   (r * math.cos(pi_over_180 * 330.), -r * math.sin(pi_over_180 * 330.)), 
                                   (r * math.cos(pi_over_180 * 210.), -r * math.sin(pi_over_180 * 210.)), 
                                   (0., -r))
        self.marker_coords['<'] = ((-r, 0.), 
                                   (r * math.cos(pi_over_180 * 60.), -r * math.sin(pi_over_180 * 60.)), 
                                   (r * math.cos(pi_over_180 * 300.), -r * math.sin(pi_over_180 * 300.)), 
                                   (-r, 0.))
        self.marker_coords['>'] = ((r, 0.), 
                                   (r * math.cos(pi_over_180 * 240.), -r * math.sin(pi_over_180 * 240.)), 
                                   (r * math.cos(pi_over_180 * 120.), -r * math.sin(pi_over_180 * 120.)), 
                                   (r, 0.))
        self.marker_coords['p'] = ((0., -r),
                                   (r2 * math.cos(pi_over_180 * 54.), -r2 * math.sin(pi_over_180 * 54.)), 
                                   (r * math.cos(pi_over_180 * 18.), -r * math.sin(pi_over_180 * 18.)), 
                                   (r2 * math.cos(pi_over_180 * 342.), -r2 * math.sin(pi_over_180 * 342.)), 
                                   (r * math.cos(pi_over_180 * 306.), -r * math.sin(pi_over_180 * 306.)), 
                                   (0., r2), 
                                   (r * math.cos(pi_over_180 * 234.), -r * math.sin(pi_over_180 * 234.)), 
                                   (r2 * math.cos(pi_over_180 * 198.), -r2 * math.sin(pi_over_180 * 198.)), 
                                   (r * math.cos(pi_over_180 * 162.), -r * math.sin(pi_over_180 * 162.)), 
                                   (r2 * math.cos(pi_over_180 * 126.), -r2 * math.sin(pi_over_180 * 126.)), 
                                   (0., -r))
        self.marker_coords['h'] = ((0., -r), 
                                   (r_over_sqrt3 * math.cos(pi_over_180 * 60.), -r_over_sqrt3 * math.sin(pi_over_180 * 60.)), 
                                   (r * math.cos(pi_over_180 * 30.), -r * math.sin(pi_over_180 * 30.)), 
                                   (r_over_sqrt3, 0.), 
                                   (r * math.cos(pi_over_180 * 330.), -r * math.sin(pi_over_180 * 330.)), 
                                   (r_over_sqrt3 * math.cos(pi_over_180 * 300.), -r_over_sqrt3 * math.sin(pi_over_180 * 300.)), 
                                   (0., r), 
                                   (r_over_sqrt3 * math.cos(pi_over_180 * 240.), -r_over_sqrt3 * math.sin(pi_over_180 * 240.)), 
                                   (r * math.cos(pi_over_180 * 210.), -r * math.sin(pi_over_180 * 210.)), 
                                   (-r_over_sqrt3, 0.), 
                                   (r * math.cos(pi_over_180 * 150.), -r * math.sin(pi_over_180 * 150.)), 
                                   (r_over_sqrt3 * math.cos(pi_over_180 * 120.), -r_over_sqrt3 * math.sin(pi_over_180 * 120.)), 
                                   (0., -r))

    def update_sizes(self):
        self.axes_left = self.canvas_left + 6. * self.label_fontsize
        self.axes_top = self.canvas_top + 3. * self.label_fontsize
        self.axes_right = self.canvas_left + self.canvas_width - 6. * self.label_fontsize
        self.axes_bottom = self.canvas_top + self.canvas_height - 4. * self.label_fontsize
        self.axes_width = self.axes_right - self.axes_left
        self.axes_height = self.axes_bottom - self.axes_top

        self.xrange = self.xlim[1] - self.xlim[0]
        self.x_pix_per_unit = self.axes_width / self.xrange
        self.x_epsilon = self.xrange / self.axes_width
        
        for yaxis in self.yaxes.keys():
            self.yaxes[yaxis].yrange = self.yaxes[yaxis].ylim[1] - self.yaxes[yaxis].ylim[0]
            self.yaxes[yaxis].y_pix_per_unit = self.axes_height / self.yaxes[yaxis].yrange
            self.yaxes[yaxis].y_epsilon = self.yaxes[yaxis].yrange / self.axes_height

    def resize(self, event):
        self.canvas_width = max(event.width - self.dw, 17. * self.label_fontsize)
        self.canvas_height = max(event.height - self.dh, 12. * self.label_fontsize)
        self.refresh_plot()

    def configure(self, **kwargs):
        self.canvas_left = float(kwargs.get('left', self.canvas_left))
        self.canvas_top = float(kwargs.get('top', self.canvas_top))
        self.canvas_width = float(kwargs.get('width', self.canvas_width))
        self.canvas_height = float(kwargs.get('height', self.canvas_height))
        self.marker_radius = float(kwargs.get('marker_radius', self.marker_radius))
        self.marker_lineweight = float(kwargs.get('marker_lineweight', self.marker_lineweight))
        self.curve_lineweight = float(kwargs.get('curve_lineweight', self.curve_lineweight))
        self.tick_length = float(kwargs.get('tick_length', self.tick_length))
        self.tick_lineweight = float(kwargs.get('tick_lineweight', self.tick_lineweight))
        self.canvas_background_color = kwargs.get('background', self.canvas_background_color)
        self.axes_background_color = kwargs.get('axes_background', self.axes_background_color)
        self.axes_color = kwargs.get('axes_color', self.axes_color)
        self.axes_lineweight = kwargs.get('axes_lineweight', self.axes_lineweight)
        self.label_font_baseline = float(kwargs.get('baseline', self.label_font_baseline))
        self.label_fontsize = int(kwargs.get('fontsize', self.label_fontsize))
        self.label_font = kwargs.get('font', self.label_font)

        self.init_markers(self.marker_radius)
        self.canvas.configure(background = self.canvas_background_color, highlightbackground = self.canvas_background_color)
        self.refresh_plot()

    def clear_plot(self, **kwargs):
        yaxis = kwargs.get('yaxis', 'all')
        if (yaxis != 'all') and (yaxis not in self.yaxes.keys()):
            raise ValueError('specified y-axis does not exist')

        if yaxis == 'all':
            self.curves = {}
        else:
            for name in self.curves.keys():
                if self.curves[name].yaxis == yaxis:
                    del(self.curves[name])
        
        self.refresh_plot()

    def draw_now(self):
        self.root.update()

    def refresh_plot(self):
        self.find_axes_limits()
        self.update_sizes()
        self.find_x_ticks()
        self.find_y_ticks()
        self.erase_plot()
        self.draw_plot()

    def draw_plot(self):
        self.draw_background()
        self.begin_group(name = 'axes')
        self.draw_axes_background()
        self.draw_grid()
        self.draw_x_ticks()
        self.draw_y_ticks()
        self.draw_axes()
        self.end_group()
        self.draw_curves()
        self.draw_axis_labels()

    def draw_background(self):
        self.draw_rect(coords = [self.canvas_left, self.canvas_top, self.canvas_left + self.canvas_width, self.canvas_top + self.canvas_height], outline = '', fill = self.canvas_background_color)

    def draw_axes_background(self):
        self.draw_rect(coords = [self.axes_left, self.axes_top, self.axes_right, self.axes_bottom], outline = '', fill = self.axes_background_color)

    def draw_axes(self):
        self.draw_line(coords = [self.axes_left, self.axes_top, self.axes_right, self.axes_top], fill = self.axes_color, width = self.axes_lineweight)
        self.draw_line(coords = [self.axes_right, self.axes_top, self.axes_right, self.axes_bottom], fill = self.axes_color, width = self.axes_lineweight)
        self.draw_line(coords = [self.axes_left, self.axes_bottom, self.axes_right, self.axes_bottom], fill = self.axes_color, width = self.axes_lineweight)
        self.draw_line(coords = [self.axes_left, self.axes_top, self.axes_left, self.axes_bottom], fill = self.axes_color, width = self.axes_lineweight)

    def to_canvas_x(self, x):
        return self.axes_left + self.x_pix_per_unit * (x - self.xlim[0])

    def to_canvas_y(self, y, yaxis = 'left'):
        return self.axes_top + self.yaxes[yaxis].y_pix_per_unit * (self.yaxes[yaxis].ylim[1] - y)

    def from_canvas_x(self, x):
        return self.xlim[0] + (x - self.axes_left) / self.x_pix_per_unit

    def from_canvas_y(self, y, yaxis = 'left'):
        return self.yaxes[yaxis].ylim[1] - (y - self.axes_top) / self.yaxes[yaxis].y_pix_per_unit

    def draw_marker(self, x, y, marker, color, name = ''):
        coords = []
        for [dx, dy] in self.marker_coords[marker]:
            coords.append(x + dx)
            coords.append(y + dy)
        if marker == '.':
            self.draw_oval(coords = coords, fill = self.colors[color], outline = self.colors[color], width = self.marker_lineweight, name = name)
        elif marker == 'o':
            self.draw_oval(coords = coords, outline = self.colors[color], width = self.marker_lineweight, name = name)
        else:
            self.draw_line(coords = coords, fill = self.colors[color], width = self.marker_lineweight, name = name)

    def draw_curve(self, curve):
        yaxis = self.yaxes[curve.yaxis]
        for j in range(len(curve.points_x)):
            px = curve.points_x[j]
            py = curve.points_y[j]
            if len(px) > 1:
                pts_in_axes = np.logical_and(np.logical_and(px >= self.xlim[0], px <= self.xlim[1]), np.logical_and(py >= yaxis.ylim[0], py <= yaxis.ylim[1]))
                where_pts_in_axes = np.where(pts_in_axes)[0]
                runs_where_pts_in_axes = np.split(where_pts_in_axes, np.where(np.diff(where_pts_in_axes) != 1)[0] + 1)
                for run in runs_where_pts_in_axes:
                    if len(run) > 1:
                        x = self.axes_left + self.x_pix_per_unit * (px[run] - self.xlim[0])
                        y = self.axes_top + yaxis.y_pix_per_unit * (yaxis.ylim[1] - py[run])
                        coords = np.vstack((x, y)).T.flatten().tolist()
                        self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)

                where_pts_leave_axes = np.where(np.logical_and(pts_in_axes[0:-1], pts_in_axes[1:] == False))[0]
                for i in where_pts_leave_axes:
                    NW = (py[i + 1] - yaxis.ylim[1]) * (px[i] - self.xlim[0]) - (px[i + 1] - self.xlim[0]) * (py[i] - yaxis.ylim[1])
                    NE = (py[i + 1] - py[i]) * (self.xlim[1] - px[i]) - (px[i + 1] - px[i]) * (yaxis.ylim[1] - py[i])
                    SE = (py[i + 1] - py[i]) * (self.xlim[1] - px[i]) - (px[i + 1] - px[i]) * (yaxis.ylim[0] - py[i])
                    SW = (py[i + 1] - yaxis.ylim[0]) * (px[i] - self.xlim[0]) - (px[i + 1] - self.xlim[0]) * (py[i] - yaxis.ylim[0])
                    if (NW > 0) and (NE > 0):
                        coords = [self.to_canvas_x(px[i]), self.to_canvas_y(py[i], curve.yaxis), 
                                  self.to_canvas_x(px[i] + (px[i + 1] - px[i]) * (yaxis.ylim[1] - py[i]) / (py[i + 1] - py[i])), self.axes_top]
                        self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                    elif (SE <= 0) and (SW <= 0):
                        coords = [self.to_canvas_x(px[i]), self.to_canvas_y(py[i], curve.yaxis), 
                                  self.to_canvas_x(px[i] + (px[i + 1] - px[i]) * (yaxis.ylim[0] - py[i]) / (py[i + 1] - py[i])), self.axes_bottom]
                        self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                    elif (NW <= 0) and (SW > 0):
                        coords = [self.to_canvas_x(px[i]), self.to_canvas_y(py[i], curve.yaxis), 
                                  self.axes_left, self.to_canvas_y(py[i] + (py[i + 1] - py[i]) * (self.xlim[0] - px[i]) / (px[i + 1] - px[i]), curve.yaxis)]
                        self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                    elif (NE <= 0) and (SE > 0):
                        coords = [self.to_canvas_x(px[i]), self.to_canvas_y(py[i], curve.yaxis), 
                                  self.axes_right, self.to_canvas_y(py[i] + (py[i + 1] - py[i]) * (self.xlim[1] - px[i]) / (px[i + 1] - px[i]), curve.yaxis)]
                        self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)

                where_pts_enter_axes = np.where(np.logical_and(pts_in_axes[0:-1] == False, pts_in_axes[1:]))[0]
                for i in where_pts_enter_axes:
                    NW = (py[i] - yaxis.ylim[1]) * (px[i + 1] - self.xlim[0]) - (px[i] - self.xlim[0]) * (py[i + 1] - yaxis.ylim[1])
                    NE = (py[i] - py[i + 1]) * (self.xlim[1] - px[i + 1]) - (px[i] - px[i + 1]) * (yaxis.ylim[1] - py[i + 1])
                    SE = (py[i] - py[i + 1]) * (self.xlim[1] - px[i + 1]) - (px[i] - px[i + 1]) * (yaxis.ylim[0] - py[i + 1])
                    SW = (py[i] - yaxis.ylim[0]) * (px[i + 1] - self.xlim[0]) - (px[i] - self.xlim[0]) * (py[i + 1] - yaxis.ylim[0])
                    if (NW > 0) and (NE > 0):
                        coords = [self.to_canvas_x(px[i + 1] + (px[i] - px[i + 1]) * (yaxis.ylim[1] - py[i + 1]) / (py[i] - py[i + 1])), self.axes_top, 
                                  self.to_canvas_x(px[i + 1]), self.to_canvas_y(py[i + 1], curve.yaxis)]
                        self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                    elif (SE <= 0) and (SW <= 0):
                        coords = [self.to_canvas_x(px[i + 1] + (px[i] - px[i + 1]) * (yaxis.ylim[0] - py[i + 1]) / (py[i] - py[i + 1])), self.axes_bottom, 
                                  self.to_canvas_x(px[i + 1]), self.to_canvas_y(py[i + 1], curve.yaxis)]
                        self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                    elif (NW <= 0) and (SW > 0):
                        coords = [self.axes_left, self.to_canvas_y(py[i + 1] + (py[i] - py[i + 1]) * (self.xlim[0] - px[i + 1]) / (px[i] - px[i + 1]), curve.yaxis), 
                                  self.to_canvas_x(px[i + 1]), self.to_canvas_y(py[i + 1], curve.yaxis)]
                        self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                    elif (NE <= 0) and (SE > 0):
                        coords = [self.axes_right, self.to_canvas_y(py[i + 1] + (py[i] - py[i + 1]) * (self.xlim[1] - px[i + 1]) / (px[i] - px[i + 1]), curve.yaxis), 
                                  self.to_canvas_x(px[i + 1]), self.to_canvas_y(py[i + 1], curve.yaxis)]
                        self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)

                adj_pts_left_of_axes = np.logical_and(px[0:-1] < self.xlim[0], px[1:] < self.xlim[0])
                adj_pts_right_of_axes = np.logical_and(px[0:-1] > self.xlim[1], px[1:] > self.xlim[1])
                adj_pts_below_axes = np.logical_and(py[0:-1] < yaxis.ylim[0], py[1:] < yaxis.ylim[0])
                adj_pts_above_axes = np.logical_and(py[0:-1] > yaxis.ylim[1], py[1:] > yaxis.ylim[1])
                adj_pts_on_same_side_of_axes = np.logical_or(np.logical_or(adj_pts_left_of_axes, adj_pts_right_of_axes), np.logical_or(adj_pts_below_axes, adj_pts_above_axes))
                adj_pts_outside_axes = np.logical_and(pts_in_axes[0:-1] == False, pts_in_axes[1:] == False)

                where_adj_pts_may_straddle_axes = np.where(np.logical_and(adj_pts_outside_axes, adj_pts_on_same_side_of_axes == False))[0]
                for i in where_adj_pts_may_straddle_axes:
                    if (px[i] == px[i + 1]):
                        coords = [self.to_canvas_x(px[i]), self.axes_bottom, 
                                  self.to_canvas_x(px[i]), self.axes_top]
                        self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                    elif (py[i] == py[i + 1]):
                        coords = [self.axes_left, self.to_canvas_y(py[i], curve.yaxis), 
                                  self.axes_right, self.to_canvas_y(py[i], curve.yaxis)]
                        self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                    else:
                        if px[i] < px[i + 1]:
                            x1, y1 = px[i], py[i]
                            x2, y2 = px[i + 1], py[i + 1]
                        else:
                            x1, y1 = px[i + 1], py[i + 1]
                            x2, y2 = px[i], py[i]
                        NW = (yaxis.ylim[1] - y1) * (x2 - x1) - (self.xlim[0] - x1) * (y2 - y1)
                        NE = (yaxis.ylim[1] - y1) * (x2 - x1) - (self.xlim[1] - x1) * (y2 - y1)
                        SE = (yaxis.ylim[0] - y1) * (x2 - x1) - (self.xlim[1] - x1) * (y2 - y1)
                        SW = (yaxis.ylim[0] - y1) * (x2 - x1) - (self.xlim[0] - x1) * (y2 - y1)
                        if (NW > 0) and (NE <= 0) and (SW <= 0):
                            coords = [self.axes_left, self.to_canvas_y(y1 + (y2 - y1) * (self.xlim[0] - x1) / (x2 - x1), curve.yaxis),
                                      self.to_canvas_x(x1 + (x2 - x1) * (yaxis.ylim[1] - y1) / (y2 - y1)), self.axes_top]
                            self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                        elif (NE > 0) and (NW <= 0) and (SE <= 0):
                            coords = [self.to_canvas_x(x1 + (x2 - x1) * (yaxis.ylim[1] - y1) / (y2 - y1)), self.axes_top,
                                      self.axes_right, self.to_canvas_y(y1 + (y2 - y1) * (self.xlim[1] - x1) / (x2 - x1), curve.yaxis)]
                            self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                        elif (SW <= 0) and (NW > 0) and (SE > 0):
                            coords = [self.axes_left, self.to_canvas_y(y1 + (y2 - y1) * (self.xlim[0] - x1) / (x2 - x1), curve.yaxis),
                                      self.to_canvas_x(x1 + (x2 - x1) * (yaxis.ylim[0] - y1) / (y2 - y1)), self.axes_bottom]
                            self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                        elif (SE <= 0) and (SW > 0) and (NE > 0):
                            coords = [self.to_canvas_x(x1 + (x2 - x1) * (yaxis.ylim[0] - y1) / (y2 - y1)), self.axes_bottom,
                                      self.axes_right, self.to_canvas_y(y1 + (y2 - y1) * (self.xlim[1] - x1) / (x2 - x1), curve.yaxis)]
                            self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                        elif (NW > 0) and (NE > 0) and (SW <= 0) and (SE <= 0):
                            coords = [self.axes_left, self.to_canvas_y(y1 + (y2 - y1) * (self.xlim[0] - x1) / (x2 - x1), curve.yaxis),
                                      self.axes_right, self.to_canvas_y(y1 + (y2 - y1) * (self.xlim[1] - x1) / (x2 - x1), curve.yaxis)]
                            self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)
                        elif (NW * NE < 0) and (SW * SE < 0):
                            coords = [self.to_canvas_x(x1 + (x2 - x1) * (yaxis.ylim[0] - y1) / (y2 - y1)), self.axes_bottom,
                                      self.to_canvas_x(x1 + (x2 - x1) * (yaxis.ylim[1] - y1) / (y2 - y1)), self.axes_top]
                            self.draw_line(coords = coords, fill = self.colors[curve.curve_color], dash = self.linestyles[curve.curve_style], width = self.curve_lineweight, name = curve.name)

    def draw_curves(self):
        for name in self.curves.keys():
            self.begin_group(name = name)
            curve = self.curves[name]
            yaxis = self.yaxes[curve.yaxis]
            if curve.curve_style != '':
                self.draw_curve(curve)
            if curve.marker != '':
                for i in range(len(curve.points_x)):
                    px = curve.points_x[i]
                    py = curve.points_y[i]
                    pts_in_axes = np.logical_and(np.logical_and(px > self.xlim[0] - self.x_epsilon, px < self.xlim[1] + self.x_epsilon), np.logical_and(py > yaxis.ylim[0] - yaxis.y_epsilon, py < yaxis.ylim[1] + yaxis.y_epsilon))
                    where_pts_in_axes = np.where(pts_in_axes)[0]
                    x = self.axes_left + self.x_pix_per_unit * (px[where_pts_in_axes] - self.xlim[0])
                    y = self.axes_top + yaxis.y_pix_per_unit * (yaxis.ylim[1] - py[where_pts_in_axes])
                    for j in range(len(x)):
                        self.draw_marker(x[j], y[j], curve.marker, curve.marker_color, name)
            self.end_group()

    def draw_v_grid_line(self, x):
        self.draw_line(coords = [x, self.axes_top, x, self.axes_bottom], fill = self.axes_color, dash = (1, 4), width = self.tick_lineweight)

    def draw_h_grid_line(self, y):
        self.draw_line(coords = [self.axes_left, y, self.axes_right, y], fill = self.axes_color, dash = (1, 4), width = self.tick_lineweight)

    def draw_grid(self):
        if self.grid_state == 'on':
            self.begin_group(name = 'grid')
            for [x, label] in self.x_ticks:
                self.draw_v_grid_line(self.to_canvas_x(x))
            for [x, label] in self.x_minor_ticks:
                self.draw_v_grid_line(self.to_canvas_x(x))

            for [y, label] in self.left_y_ticks:
                self.draw_h_grid_line(self.to_canvas_y(y, self.left_yaxis))
            for [y, label] in self.left_y_minor_ticks:
                self.draw_h_grid_line(self.to_canvas_y(y, self.left_yaxis))

            for [y, label] in self.right_y_ticks:
                self.draw_h_grid_line(self.to_canvas_y(y, self.right_yaxis))
            for [y, label] in self.right_y_minor_ticks:
                self.draw_h_grid_line(self.to_canvas_y(y, self.right_yaxis))
            self.end_group()

    def draw_top_tick(self, x):
        self.draw_line(coords = [x, self.axes_top, x, self.axes_top + self.tick_length], fill = self.axes_color, width = self.tick_lineweight)

    def draw_bottom_tick(self, x):
        self.draw_line(coords = [x, self.axes_bottom, x, self.axes_bottom - self.tick_length], fill = self.axes_color, width = self.tick_lineweight)

    def draw_left_tick(self, y):
        self.draw_line(coords = [self.axes_left, y, self.axes_left + self.tick_length, y], fill = self.axes_color, width = self.tick_lineweight)

    def draw_right_tick(self, y):
        self.draw_line(coords = [self.axes_right, y, self.axes_right - self.tick_length, y], fill = self.axes_color, width = self.tick_lineweight)

    def draw_top_minor_tick(self, x):
        self.draw_line(coords = [x, self.axes_top, x, self.axes_top + 0.5 * self.tick_length], fill = self.axes_color, width = self.tick_lineweight)

    def draw_bottom_minor_tick(self, x):
        self.draw_line(coords = [x, self.axes_bottom, x, self.axes_bottom - 0.5 * self.tick_length], fill = self.axes_color, width = self.tick_lineweight)

    def draw_left_minor_tick(self, y):
        self.draw_line(coords = [self.axes_left, y, self.axes_left + 0.5 * self.tick_length, y], fill = self.axes_color, width = self.tick_lineweight)

    def draw_right_minor_tick(self, y):
        self.draw_line(coords = [self.axes_right, y, self.axes_right - 0.5 * self.tick_length, y], fill = self.axes_color, width = self.tick_lineweight)

    def draw_bottom_tick_label(self, x, label):
        self.draw_text(coords = [x, self.axes_bottom + 0.5 * self.label_fontsize], text = label, font = (self.label_font, self.label_fontsize), fill = self.axes_color, anchor = 'n', justify = 'center')

    def draw_left_tick_label(self, y, label, label_color):
        self.draw_text(coords = [self.axes_left - 0.5 * self.label_fontsize, y], text = label, font = (self.label_font, self.label_fontsize), fill = self.axes_color, anchor = 'e', justify = 'right')

    def draw_right_tick_label(self, y, label, label_color):
        self.draw_text(coords = [self.axes_right + 0.5 * self.label_fontsize, y], text = label, font = (self.label_font, self.label_fontsize), fill = self.axes_color, anchor = 'w', justify = 'left')

    def draw_x_ticks(self):
        if (len(self.x_ticks) != 0) or (len(self.x_minor_ticks) != 0):
            self.begin_group(name = 'x_ticks')
            for [x, label] in self.x_ticks:
                self.draw_top_tick(self.to_canvas_x(x))
                self.draw_bottom_tick(self.to_canvas_x(x))
            for [x, label] in self.x_minor_ticks:
                self.draw_top_minor_tick(self.to_canvas_x(x))
                self.draw_bottom_minor_tick(self.to_canvas_x(x))
            self.end_group()
            self.begin_group(name = 'x_ticklabels')
            for [x, label] in self.x_ticks:
                if label != '':
                    self.draw_bottom_tick_label(self.to_canvas_x(x), label)
            for [x, label] in self.x_minor_ticks:
                if label != '':
                    self.draw_bottom_tick_label(self.to_canvas_x(x), label)
            self.end_group()

    def draw_y_ticks(self):
        left_curves = [curve_name for curve_name in self.curves if self.curves[curve_name].yaxis == self.left_yaxis]
        right_curves = [curve_name for curve_name in self.curves if self.curves[curve_name].yaxis == self.right_yaxis]
        if (self.left_yaxis != '') and ((self.right_yaxis == '') or (len(right_curves) == 0)):
            if (len(self.left_y_ticks) != 0) or (len(self.left_y_minor_ticks) != 0):
                self.begin_group(name = 'y_ticks')
                for [y, label] in self.left_y_ticks:
                    self.draw_left_tick(self.to_canvas_y(y, self.left_yaxis))
                    self.draw_right_tick(self.to_canvas_y(y, self.left_yaxis))
                for [y, label] in self.left_y_minor_ticks:
                    self.draw_left_minor_tick(self.to_canvas_y(y, self.left_yaxis))
                    self.draw_right_minor_tick(self.to_canvas_y(y, self.left_yaxis))
                self.end_group()
                self.begin_group(name = 'y_ticklabels')
                for [y, label] in self.left_y_ticks:
                    if label != '':
                        self.draw_left_tick_label(self.to_canvas_y(y, self.left_yaxis), label, self.yaxes[self.left_yaxis].color)
                for [y, label] in self.left_y_minor_ticks:
                    if label != '':
                        self.draw_left_tick_label(self.to_canvas_y(y, self.left_yaxis), label, self.yaxes[self.left_yaxis].color)
                self.end_group()
        elif ((self.left_yaxis == '') or (len(left_curves) == 0)) and (self.right_yaxis != ''):
            if (len(self.right_y_ticks) != 0) or (len(self.right_y_minor_ticks) != 0):
                self.begin_group(name = 'y_ticks')
                for [y, label] in self.right_y_ticks:
                    self.draw_left_tick(self.to_canvas_y(y, self.right_yaxis))
                    self.draw_right_tick(self.to_canvas_y(y, self.right_yaxis))
                for [y, label] in self.right_y_minor_ticks:
                    self.draw_left_minor_tick(self.to_canvas_y(y, self.right_yaxis))
                    self.draw_right_minor_tick(self.to_canvas_y(y, self.right_yaxis))
                self.end_group()
                self.begin_group(name = 'y_ticklabels')
                for [y, label] in self.right_y_ticks:
                    if label != '':
                        self.draw_right_tick_label(self.to_canvas_y(y, self.right_yaxis), label, self.yaxes[self.right_yaxis].color)
                for [y, label] in self.right_y_minor_ticks:
                    if label != '':
                        self.draw_right_tick_label(self.to_canvas_y(y, self.right_yaxis), label, self.yaxes[self.right_yaxis].color)
                self.end_group()
        elif (self.left_yaxis != '') and (self.right_yaxis != ''):
            if (len(self.left_y_ticks) != 0) or (len(self.left_y_minor_ticks) != 0) or (len(self.right_y_ticks) != 0) or (len(self.right_y_minor_ticks) != 0):
                self.begin_group(name = 'left_y_ticks')
                for [y, label] in self.left_y_ticks:
                    self.draw_left_tick(self.to_canvas_y(y, self.left_yaxis))
                for [y, label] in self.left_y_minor_ticks:
                    self.draw_left_minor_tick(self.to_canvas_y(y, self.left_yaxis))
                self.end_group()
                self.begin_group(name = 'left_y_ticklabels')
                for [y, label] in self.left_y_ticks:
                    if label != '':
                        self.draw_left_tick_label(self.to_canvas_y(y, self.left_yaxis), label, self.yaxes[self.left_yaxis].color)
                for [y, label] in self.left_y_minor_ticks:
                    if label != '':
                        self.draw_left_tick_label(self.to_canvas_y(y, self.left_yaxis), label, self.yaxes[self.left_yaxis].color)
                self.end_group()
                self.begin_group(name = 'right_y_ticks')
                for [y, label] in self.right_y_ticks:
                    self.draw_right_tick(self.to_canvas_y(y, self.right_yaxis))
                for [y, label] in self.right_y_minor_ticks:
                    self.draw_right_minor_tick(self.to_canvas_y(y, self.right_yaxis))
                self.end_group()
                self.begin_group(name = 'right_y_ticklabels')
                for [y, label] in self.right_y_ticks:
                    if label != '':
                        self.draw_right_tick_label(self.to_canvas_y(y, self.right_yaxis), label, self.yaxes[self.right_yaxis].color)
                for [y, label] in self.right_y_minor_ticks:
                    if label != '':
                        self.draw_right_tick_label(self.to_canvas_y(y, self.right_yaxis), label, self.yaxes[self.right_yaxis].color)
                self.end_group()

    def draw_axis_labels(self):
        if self.xlabel_value != '':
           self.draw_text(coords = [0.5 * (self.axes_left + self.axes_right), self.axes_bottom + 2.5 * self.label_fontsize], text = self.xlabel_value, font = (self.label_font, self.label_fontsize), fill = self.axes_color, anchor = 'n', justify = 'center')
        if self.left_yaxis != '':
            if self.yaxes[self.left_yaxis].ylabel_value != '':
                self.draw_text(coords = [self.axes_left, self.axes_top - 0.5 * self.label_fontsize], text = self.yaxes[self.left_yaxis].ylabel_value, font = (self.label_font, self.label_fontsize), fill = self.yaxes[self.left_yaxis].color, anchor = 'sw', justify = 'left')
        if self.right_yaxis != '':
            if self.yaxes[self.right_yaxis].ylabel_value != '':
                self.draw_text(coords = [self.axes_right, self.axes_top - 0.5 * self.label_fontsize], text = self.yaxes[self.right_yaxis].ylabel_value, font = (self.label_font, self.label_fontsize), fill = self.yaxes[self.right_yaxis].color, anchor = 'se', justify = 'right')

    def find_x_ticks(self):
        self.x_ticks = []
        self.x_minor_ticks = []
        if self.curves != {}:
            if self.xaxis_mode == 'linear':
                self.x_ticks = self.find_linear_ticks(self.xlimits_mode, self.axes_width, self.xrange, self.xlim, self.x_epsilon, self.xmin, self.xmax)
                self.x_minor_ticks = []
            elif self.xaxis_mode == 'log':
                self.x_ticks = self.find_log_ticks(self.xlimits_mode, self.axes_width, self.xrange, self.xlim, self.x_epsilon, self.xaxis_sign, self.xmin, self.xmax)
                self.x_minor_ticks = self.find_log_minor_ticks(self.axes_width, self.xrange, self.xlim, self.x_epsilon, self.xaxis_sign, self.xmin, self.xmax)

    def find_y_ticks(self):
        self.left_y_ticks = []
        self.left_y_minor_ticks = []
        self.right_y_ticks = []
        self.right_y_minor_ticks = []
        left_curves = [curve_name for curve_name in self.curves if self.curves[curve_name].yaxis == self.left_yaxis]
        right_curves = [curve_name for curve_name in self.curves if self.curves[curve_name].yaxis == self.right_yaxis]
        if self.curves != {}:
            if (self.left_yaxis != '') and (len(left_curves) != 0):
                yaxis = self.yaxes[self.left_yaxis]
                if yaxis.yaxis_mode == 'linear':
                    self.left_y_ticks = self.find_linear_ticks(yaxis.ylimits_mode, self.axes_height, yaxis.yrange, yaxis.ylim, yaxis.y_epsilon, yaxis.ymin, yaxis.ymax)
                    self.left_y_minor_ticks = []
                elif yaxis.yaxis_mode == 'log':
                    self.left_y_ticks = self.find_log_ticks(yaxis.ylimits_mode, self.axes_height, yaxis.yrange, yaxis.ylim, yaxis.y_epsilon, yaxis.yaxis_sign, yaxis.ymin, yaxis.ymax)
                    self.left_y_minor_ticks = self.find_log_minor_ticks(self.axes_height, yaxis.yrange, yaxis.ylim, yaxis.y_epsilon, yaxis.yaxis_sign, yaxis.ymin, yaxis.ymax)
            if (self.right_yaxis != '') and (len(right_curves) != 0):
                yaxis = self.yaxes[self.right_yaxis]
                if yaxis.yaxis_mode == 'linear':
                    self.right_y_ticks = self.find_linear_ticks(yaxis.ylimits_mode, self.axes_height, yaxis.yrange, yaxis.ylim, yaxis.y_epsilon, yaxis.ymin, yaxis.ymax)
                    self.right_y_minor_ticks = []
                elif yaxis.yaxis_mode == 'log':
                    self.right_y_ticks = self.find_log_ticks(yaxis.ylimits_mode, self.axes_height, yaxis.yrange, yaxis.ylim, yaxis.y_epsilon, yaxis.yaxis_sign, yaxis.ymin, yaxis.ymax)
                    self.right_y_minor_ticks = self.find_log_minor_ticks(self.axes_height, yaxis.yrange, yaxis.ylim, yaxis.y_epsilon, yaxis.yaxis_sign, yaxis.ymin, yaxis.ymax)

    def find_linear_ticks(self, axis_limits_mode, axis_dimension, axis_range, axis_lim, epsilon, axis_min, axis_max):
        if axis_limits_mode == 'auto':
            axis_range = axis_max - axis_min
        tick_interval = axis_range / min(10., axis_dimension / (2.5 * self.label_fontsize))
        foo = math.log10(tick_interval)
        bar = math.floor(foo)
        foobar = foo - bar
        if foobar < 0.001:
            tick_interval = math.pow(10., bar)
        elif foobar < math.log10(2.001):
            tick_interval = 2. * math.pow(10., bar)
        elif foobar < math.log10(5.001):
            tick_interval = 5. * math.pow(10., bar)
        else:
            tick_interval = 10. * math.pow(10., bar)
        if axis_limits_mode == 'auto':
            axis_lim[0] = tick_interval * math.floor(axis_min / tick_interval)
            axis_lim[1] = tick_interval * math.ceil(axis_max / tick_interval)
            self.update_sizes()
        tick = tick_interval * round(axis_lim[0] / tick_interval)
        ticks = []
        for i in range(int(math.ceil((axis_lim[1] - axis_lim[0]) / tick_interval)) + 1):
            if (tick > axis_lim[0] - epsilon) and (tick < axis_lim[1] + epsilon):
                ticks.append(tick_interval * round(tick / tick_interval))
            tick += tick_interval

        if len(ticks) != 0:
            if (min(ticks) == 0.) and (max(ticks) == 0.):
                foo = 0
            else:
                foo = int(math.floor(math.log10(max(abs(min(ticks)), abs(max(ticks)), axis_range)) / 3.))
        axis_ticks = []
        for tick in ticks:
            if (foo >= -8) and (foo <= 8):
                if tick == -0.:
                    tick = 0.
                tick_label = str(self.multipliers[foo] * tick)
                if tick_label[-2:] == '.0':
                    tick_label = tick_label.replace('.0', '')
                axis_ticks.append([tick, tick_label + self.prefixes[foo]])
            else:
                axis_ticks.append([tick, str(tick)])
        return axis_ticks

    def find_log_ticks(self, axis_limits_mode, axis_dimension, axis_range, axis_lim, epsilon, sign, axis_min, axis_max):
        if axis_limits_mode == 'auto':
            axis_range = axis_max - axis_min
        tick_interval = math.ceil(axis_range / min(10., axis_dimension / (2.5 * self.label_fontsize)))
        if axis_limits_mode == 'auto':
            axis_lim[0] = tick_interval * math.floor(axis_min / tick_interval)
            axis_lim[1] = tick_interval * math.ceil(axis_max / tick_interval)
            self.update_sizes()
        tick = tick_interval * round(axis_lim[0] / tick_interval)
        ticks = []
        for i in range(int(math.ceil((axis_lim[1] - axis_lim[0]) / tick_interval)) + 1):
            if (tick > axis_lim[0] - epsilon) and (tick < axis_lim[1] + epsilon):
                ticks.append(tick_interval * round(tick / tick_interval))
            tick += tick_interval
        axis_ticks = []
        for tick in ticks:
            foo = int(math.floor(sign * tick / 3.))
            if (foo >= -8) and (foo <= 8):
                tick_label = str(sign * round(self.multipliers[foo] * math.pow(10., sign * tick)))
                if tick_label[-2:] == '.0':
                    tick_label = tick_label.replace('.0', '')
                axis_ticks.append([tick, tick_label + self.prefixes[foo]])
            else:
                axis_ticks.append([tick, str(sign * math.pow(10., sign * tick))])
        return axis_ticks

    def find_log_minor_ticks(self, axis_dimension, axis_range, axis_lim, epsilon, sign, axis_min, axis_max):
        minor_ticks = []
        tick_interval = axis_range / min(10., axis_dimension / (2.5 * self.label_fontsize))
        minor_tick_interval = 10. * min(1. - math.pow(10., -tick_interval), math.pow(10., tick_interval) - 1.)
        tick_interval = math.ceil(tick_interval)
        foo = math.log10(minor_tick_interval)
        bar = math.floor(foo)
        foobar = foo - bar
        if foobar < 0.001:
            minor_tick_interval = math.pow(10., bar)
        elif foobar < math.log10(2.001):
            minor_tick_interval = 2. * math.pow(10., bar)
        elif foobar < math.log10(5.001):
            minor_tick_interval = 5. * math.pow(10., bar)
        else:
            minor_tick_interval = 10. * math.pow(10., bar)
        if (tick_interval == 1.) and (axis_range <= 1.):
            label_threshold = 2.5 * self.label_fontsize * epsilon
            if minor_tick_interval < 1.:
                ticks_to_label = []
                tick = 1. + minor_tick_interval
                while tick < 10. - 0.001 * minor_tick_interval:
                    ticks_to_label.append(tick)
                    tick += minor_tick_interval
            elif math.log10(10. / 9.) > label_threshold:
                ticks_to_label = range(2, 10)
            elif math.log10(1.25) > label_threshold:
                ticks_to_label = range(2, 10, 2)
            elif math.log10(2) > label_threshold:
                ticks_to_label = [2, 5]
            elif math.log10(3) > label_threshold:
                ticks_to_label = [3]
            else:
                ticks_to_label = []
            for i in range(int(math.ceil(axis_range)) + 2):
                exponent = math.floor(axis_lim[0]) + i
                for j in ticks_to_label:
                    minor_tick = exponent + sign * math.log10(float(j))
                    if (minor_tick > axis_lim[0] - epsilon) and (minor_tick < axis_lim[1] + epsilon):
                        foo = int(math.floor(sign * minor_tick / 3.))
                        if (foo >= -8) and (foo <= 8):
                            tick_label = str(sign * self.multipliers[foo] * math.pow(10., sign * minor_tick))
                            if tick_label[-2:] == '.0':
                                tick_label = tick_label.replace('.0', '')
                            minor_ticks.append([minor_tick, tick_label + self.prefixes[foo]])
                        else:
                            minor_ticks.append([minor_tick, str(sign * math.pow(10., sign * minor_tick))])
        elif (tick_interval == 1.) and (math.log10(10. / 9.) > 2. * epsilon):
            for i in range(int(math.ceil(axis_range)) + 2):
                exponent = math.floor(axis_lim[0]) + i
                for j in range(2, 10):
                    minor_tick = exponent + sign * math.log10(float(j))
                    if (minor_tick > axis_lim[0] - epsilon) and (minor_tick < axis_lim[1] + epsilon):
                        minor_ticks.append([minor_tick, ''])
        elif (tick_interval > 1.) and (epsilon < 0.25):
            for i in range(int(math.ceil(axis_range)) + 2):
                minor_tick = math.floor(axis_lim[0]) + i
                if (minor_tick > axis_lim[0] - epsilon) and (minor_tick < axis_lim[1] + epsilon) and (minor_tick != tick_interval * round(minor_tick / tick_interval)):
                    minor_ticks.append([minor_tick, ''])
        return minor_ticks
 
    def find_axes_limits(self):
        if self.curves != {}:
            if self.xlimits_mode != 'manual':
                x_mins = []
                x_maxs = []
                for curve_name in self.curves.keys():
                    curve = self.curves[curve_name]
                    yaxis = self.yaxes[curve.yaxis]
                    if yaxis.ylimits_mode == 'manual':
                        for i in range(len(curve.points_x)):
                            pts_where_y_in_axes = np.where(np.logical_and(curve.points_y[i] > yaxis.ylim[0] - yaxis.y_epsilon, curve.points_y[i] < yaxis.ylim[1] + yaxis.y_epsilon))[0]
                            if len(pts_where_y_in_axes) != 0:
                                x_mins.append(np.amin(curve.points_x[i][pts_where_y_in_axes]))
                                x_maxs.append(np.amax(curve.points_x[i][pts_where_y_in_axes]))
                    else:
                        for i in range(len(curve.points_x)):
                            if len(curve.points_x[i]) != 0:
                                x_mins.append(np.amin(curve.points_x[i]))
                                x_maxs.append(np.amax(curve.points_x[i]))
                if (len(x_mins) > 0) and (len(x_maxs) > 0):
                    self.xlim[0] = min(x_mins)
                    self.xlim[1] = max(x_maxs)
                    if self.xlim[0] == self.xlim[1]:
                        if self.xlim[0] > 0.:
                            self.xlim[0] = 0.95 * self.xlim[0]
                            self.xlim[1] = 1.05 * self.xlim[1]
                        elif self.xlim[0] < 0.:
                            self.xlim[0] = 1.05 * self.xlim[0]
                            self.xlim[1] = 0.95 * self.xlim[1]
                        else:
                            self.xlim[0] = -0.05
                            self.xlim[1] = 0.05
                    self.xmin = self.xlim[0]
                    self.xmax = self.xlim[1]
            for yaxis_name in self.yaxes.keys():
                yaxis = self.yaxes[yaxis_name]
                if yaxis.ylimits_mode != 'manual':
                    y_mins = []
                    y_maxs = []
                    for curve_name in self.curves.keys():
                        curve = self.curves[curve_name]
                        if curve.yaxis == yaxis_name:
                            if self.xlimits_mode == 'manual':
                                for i in range(len(curve.points_y)):
                                    pts_where_x_in_axes = np.where(np.logical_and(curve.points_x[i] > self.xlim[0] - self.x_epsilon, curve.points_x[i] < self.xlim[1] + self.x_epsilon))[0]
                                    if len(pts_where_x_in_axes) != 0:
                                        y_mins.append(np.amin(curve.points_y[i][pts_where_x_in_axes]))
                                        y_maxs.append(np.amax(curve.points_y[i][pts_where_x_in_axes]))
                            else:
                                for i in range(len(curve.points_y)):
                                    if len(curve.points_y[i]) != 0:
                                        y_mins.append(np.amin(curve.points_y[i]))
                                        y_maxs.append(np.amax(curve.points_y[i]))
                    if (len(y_mins) > 0) and (len(y_maxs) > 0):
                        yaxis.ylim[0] = min(y_mins)
                        yaxis.ylim[1] = max(y_maxs)
                        if yaxis.ylim[0] == yaxis.ylim[1]:
                            if yaxis.ylim[0] > 0.:
                                yaxis.ylim[0] = 0.95 * yaxis.ylim[0]
                                yaxis.ylim[1] = 1.05 * yaxis.ylim[1]
                            elif yaxis.ylim[0] < 0.:
                                yaxis.ylim[0] = 1.05 * yaxis.ylim[0]
                                yaxis.ylim[1] = 0.95 * yaxis.ylim[1]
                            else:
                                yaxis.ylim[0] = -0.05
                                yaxis.ylim[1] = 0.05
                        yaxis.ymin = yaxis.ylim[0]
                        yaxis.ymax = yaxis.ylim[1]

    def parse_style(self, style):
        length = len(style)
        colors = self.colors.keys()
        markers = self.marker_coords.keys()
        linestyles = self.linestyles.keys()
        marker_color = ''
        marker = ''
        curve_color = ''
        curve_style = ''
        if (length >= 1) and (style[0] in colors):
            if (length >= 2) and (style[1] in markers):
                marker_color = style[0]
                marker = style[1]
                if (length >= 3) and (style[2] in colors):
                    curve_color = style[2]
                    if (length >= 5) and (style[3:5] in linestyles):
                        curve_style = style[3:5]
                    elif (length >= 4) and (style[3] in linestyles):
                        curve_style = style[3]
                elif (length >= 4) and (style[2:4] in linestyles):
                    curve_style = style[2:4]
                elif (length >= 3) and (style[2] in linestyles):
                    curve_style = style[2]
            elif (length >= 3) and (style[1:3] in linestyles):
                curve_color = style[0]
                curve_style = style[1:3]
            elif (length >= 2) and (style[1] in linestyles):
                curve_color = style[0]
                curve_style = style[1]
        elif (length >= 1) and (style[0] in markers):
            marker = style[0]
            if (length >= 2) and (style[1] in colors):
                curve_color = style[1]
                if (length >= 4) and (style[2:4] in linestyles):
                    curve_style = style[2:4]
                elif (length >= 3) and (style[2] in linestyles):
                    curve_style = style[2]
            elif (length >= 3) and (style[1:3] in linestyles):
                curve_style = style[1:3]
            elif (length >= 2) and (style[1] in linestyles):
                curve_style = style[1]
        elif (length >= 2) and (style[0:2] in linestyles):
            curve_style = style[0:2]
        elif (length >= 1) and (style[0] in linestyles):
            curve_style = style[0]
        if (marker == '') and (curve_style == ''):
            marker = self.default_marker
            curve_style = self.default_curve_style
        if ((marker != '') and (marker_color == '')) or ((curve_style != '') and (curve_color == '')):
            if marker_color == '':
                marker_color = self.default_color_order[self.default_color_index]
            if curve_color == '':
                curve_color = self.default_color_order[self.default_color_index]
            self.default_color_index = self.default_color_index + 1
            if self.default_color_index >= len(self.default_color_order):
                self.default_color_index = 0
        if (marker_color != '') and (curve_color == ''):
            curve_color = marker_color
        if (marker_color == '') and (curve_color != ''):
            marker_color = curve_color
        return [marker_color, marker, curve_color, curve_style]

    def new_data(self, x, y, style = '', name = '', yaxis = 'left', hold = 'off'):
        new_curves = {}
        if type(x) is np.ndarray:
            if type(y) is np.ndarray:
                if len(x) == len(y):
                    if name != '':
                        curve_name = name
                    else:
                        curve_name = 'curve{0:05d}'.format(self.curve_id)
                        self.curve_id += 1
                    new_curves[curve_name] = self.curve(name = curve_name, yaxis = yaxis, data_x = x.copy(), data_y = y.copy())
                    [new_curves[curve_name].marker_color, new_curves[curve_name].marker, new_curves[curve_name].curve_color, new_curves[curve_name].curve_style] = self.parse_style(style)
                else:
                    raise IndexError('x and y numpy arrays supplied did not have the same number of elements')
            elif (type(y) is list) and all([type(v) is np.ndarray for v in y]):
                if all([len(x) == len(v) for v in y]):
                    for j in range(len(y)):
                        if (type(name) is list) and name[j] != '':
                            curve_name = name[j]
                        else:
                            curve_name = 'curve{0:05d}'.format(self.curve_id)
                            self.curve_id += 1
                        new_curves[curve_name] = self.curve(name = curve_name, yaxis = yaxis, data_x = x.copy(), data_y = y[j].copy())
                        if type(style) is str:
                            [new_curves[curve_name].marker_color, new_curves[curve_name].marker, new_curves[curve_name].curve_color, new_curves[curve_name].curve_style] = self.parse_style(style)
                        else:
                            [new_curves[curve_name].marker_color, new_curves[curve_name].marker, new_curves[curve_name].curve_color, new_curves[curve_name].curve_style] = self.parse_style(style[j])
                else:
                    raise IndexError('at least one of the numpy arrays supplied in y did not have the same number of elements as x')
            else:
                raise TypeError('if x is a numpy array, y must either be a numpy array or a list of numpy arrays')
        elif (type(x) is list) and all([type(v) is np.ndarray for v in x]):
            if (type(y) is list) and all([type(v) is np.ndarray for v in y]):
                if len(x) == len(y):
                    if all([len(x[j]) == len(y[j]) for j in range(len(x))]):
                        for j in range(len(x)):
                            if (type(name) is list) and name[j] != '':
                                curve_name = name[j]
                            else:
                                curve_name = 'curve{0:05d}'.format(self.curve_id)
                                self.curve_id += 1
                            new_curves[curve_name] = self.curve(name = curve_name, yaxis = yaxis, data_x = x[j].copy(), data_y = y[j].copy())
                            if type(style) is str:
                                [new_curves[curve_name].marker_color, new_curves[curve_name].marker, new_curves[curve_name].curve_color, new_curves[curve_name].curve_style] = self.parse_style(style)
                            else:
                                [new_curves[curve_name].marker_color, new_curves[curve_name].marker, new_curves[curve_name].curve_color, new_curves[curve_name].curve_style] = self.parse_style(style[j])
                    else:
                        raise IndexError('at least one of the numpy arrays supplied in x did not have the same number of elements as the corresponding numpy arrays supplied in y')
                else:
                    raise IndexError('x and y supplied did not contain the same number of numpy arrays')
            else:
                raise TypeError('if x is a list of numpy arrays, y must also be a list of numpy arrays')
        else:
            raise TypeError('x and y supplied were not numpy arrays or lists of numpy arrays')
        if hold == 'off':
            self.curves = new_curves
        else:
            self.curves.update(new_curves)

    def plot(self, x, y, style = '', **kwargs):
        name = kwargs.get('name', '')

        yaxis = kwargs.get('yaxis', 'left')
        if yaxis not in self.yaxes.keys():
            raise ValueError("specified y-axis does not exist")

        hold = kwargs.get('hold', 'off')
        if hold not in ('on', 'off'):
            raise ValueError("if specified, hold must be 'on' or 'off'")
        if hold == 'off':
            self.default_color_index = 0

        self.new_data(x, y, style, name, yaxis, hold)

        self.xaxis_mode = 'linear'
        self.xlimits_mode = 'auto'

        self.yaxes[yaxis].yaxis_mode = 'linear'
        self.yaxes[yaxis].ylimits_mode = 'auto'

        for curve_name in self.curves.keys():
            curve = self.curves[curve_name]
            yaxis = self.yaxes[curve.yaxis]
            if yaxis.yaxis_mode == 'linear':
                curve.points_x = [curve.data_x.copy()]
                curve.points_y = [curve.data_y.copy()]
            elif yaxis.yaxis_mode == 'log':
                where_y_has_same_sign_as_yaxis = np.where(curve.data_y * yaxis.yaxis_sign > 0.)[0]
                runs_where_y_has_same_sign_as_yaxis = np.split(where_y_has_same_sign_as_yaxis, np.where(np.diff(where_y_has_same_sign_as_yaxis) != 1)[0] + 1)
                curve.points_x = [curve.data_x[run].copy() for run in runs_where_y_has_same_sign_as_yaxis]
                curve.points_y = [yaxis.yaxis_sign * np.log10(yaxis.yaxis_sign * curve.data_y[run]) for run in runs_where_y_has_same_sign_as_yaxis]

        self.refresh_plot()

    def semilogx(self, x, y, style = '', **kwargs):
        name = kwargs.get('name', '')

        yaxis = kwargs.get('yaxis', 'left')
        if yaxis not in self.yaxes.keys():
            raise ValueError("specified y-axis does not exist")

        hold = kwargs.get('hold', 'off')
        if hold not in ('on', 'off'):
            raise ValueError("if specified, hold must be 'on' or 'off'")
        if hold == 'off':
            self.default_color_index = 0

        self.new_data(x, y, style, name, yaxis, hold)

        self.xaxis_mode = 'log'
        pos_x_values = 0
        total_x_values = 0
        for curve_name in self.curves.keys():
            pos_x_values += len(np.where(self.curves[curve_name].data_x > 0.)[0])
            total_x_values += len(self.curves[curve_name].data_x)
        self.xaxis_sign = 1. if pos_x_values >= total_x_values // 2 else -1.
        self.xlimits_mode = 'auto'

        self.yaxes[yaxis].yaxis_mode = 'linear'
        self.yaxes[yaxis].ylimits_mode = 'auto'

        for curve_name in self.curves.keys():
            curve = self.curves[curve_name]
            yaxis = self.yaxes[curve.yaxis]
            if yaxis.yaxis_mode == 'linear':
                where_x_has_same_sign_as_xaxis = np.where(curve.data_x * self.xaxis_sign > 0.)[0]
                runs_where_x_has_same_sign_as_xaxis = np.split(where_x_has_same_sign_as_xaxis, np.where(np.diff(where_x_has_same_sign_as_xaxis) != 1)[0] + 1)
                curve.points_x = [self.xaxis_sign * np.log10(self.xaxis_sign * curve.data_x[run]) for run in runs_where_x_has_same_sign_as_xaxis]
                curve.points_y = [curve.data_y[run].copy() for run in runs_where_x_has_same_sign_as_xaxis]
            elif yaxis.yaxis_mode == 'log':
                where_xy_have_same_sign_as_axes = np.where(np.logical_and(curve.data_x * self.xaxis_sign > 0., curve.data_y * yaxis.yaxis_sign > 0.))[0]
                runs_where_xy_have_same_sign_as_axes = np.split(where_xy_have_same_sign_as_axes, np.where(np.diff(where_xy_have_same_sign_as_axes) != 1)[0] + 1)
                curve.points_x = [self.xaxis_sign * np.log10(self.xaxis_sign * curve.data_x[run]) for run in runs_where_xy_have_same_sign_as_axes]
                curve.points_y = [yaxis.yaxis_sign * np.log10(yaxis.yaxis_sign * curve.data_y[run]) for run in runs_where_xy_have_same_sign_as_axes]

        self.refresh_plot()

    def semilogy(self, x, y, style = '', **kwargs):
        name = kwargs.get('name', '')

        yaxis = kwargs.get('yaxis', 'left')
        if yaxis not in self.yaxes.keys():
            raise ValueError("specified y-axis does not exist")

        hold = kwargs.get('hold', 'off')
        if hold not in ('on', 'off'):
            raise ValueError("if specified, hold must be 'on' or 'off'")
        if hold == 'off':
            self.default_color_index = 0

        self.new_data(x, y, style, name, yaxis, hold)

        self.xaxis_mode = 'linear'
        self.xlimits_mode = 'auto'

        self.yaxes[yaxis].yaxis_mode = 'log'
        pos_y_values = 0
        total_y_values = 0
        for curve_name in self.curves.keys():
            if self.curves[curve_name].yaxis == yaxis:
                pos_y_values += len(np.where(self.curves[curve_name].data_y > 0.)[0])
                total_y_values += len(self.curves[curve_name].data_y)
        self.yaxes[yaxis].yaxis_sign = 1. if pos_y_values >= total_y_values // 2 else -1.
        self.yaxes[yaxis].ylimits_mode = 'auto'

        for curve_name in self.curves.keys():
            curve = self.curves[curve_name]
            yaxis = self.yaxes[curve.yaxis]
            if yaxis.yaxis_mode == 'linear':
                curve.points_x = [curve.data_x.copy()]
                curve.points_y = [curve.data_y.copy()]
            elif yaxis.yaxis_mode == 'log':
                where_y_has_same_sign_as_yaxis = np.where(curve.data_y * yaxis.yaxis_sign > 0.)[0]
                runs_where_y_has_same_sign_as_yaxis = np.split(where_y_has_same_sign_as_yaxis, np.where(np.diff(where_y_has_same_sign_as_yaxis) != 1)[0] + 1)
                curve.points_x = [curve.data_x[run].copy() for run in runs_where_y_has_same_sign_as_yaxis]
                curve.points_y = [yaxis.yaxis_sign * np.log10(yaxis.yaxis_sign * curve.data_y[run]) for run in runs_where_y_has_same_sign_as_yaxis]

        self.refresh_plot()

    def loglog(self, x, y, style = '', **kwargs):
        name = kwargs.get('name', '')

        yaxis = kwargs.get('yaxis', 'left')
        if yaxis not in self.yaxes.keys():
            raise ValueError("specified y-axis does not exist")

        hold = kwargs.get('hold', 'off')
        if hold not in ('on', 'off'):
            raise ValueError("if specified, hold must be 'on' or 'off'")
        if hold == 'off':
            self.default_color_index = 0

        self.new_data(x, y, style, name, yaxis, hold)

        self.xaxis_mode = 'log'
        pos_x_values = 0
        total_x_values = 0
        for curve_name in self.curves.keys():
            pos_x_values += len(np.where(self.curves[curve_name].data_x > 0.)[0])
            total_x_values += len(self.curves[curve_name].data_x)
        self.xaxis_sign = 1. if pos_x_values >= total_x_values // 2 else -1.
        self.xlimits_mode = 'auto'

        self.yaxes[yaxis].yaxis_mode = 'log'
        pos_y_values = 0
        total_y_values = 0
        for curve_name in self.curves.keys():
            if self.curves[curve_name].yaxis == yaxis:
                pos_y_values += len(np.where(self.curves[curve_name].data_y > 0.)[0])
                total_y_values += len(self.curves[curve_name].data_y)
        self.yaxes[yaxis].yaxis_sign = 1. if pos_y_values >= total_y_values // 2 else -1.
        self.yaxes[yaxis].ylimits_mode = 'auto'

        for curve_name in self.curves.keys():
            curve = self.curves[curve_name]
            yaxis = self.yaxes[curve.yaxis]
            if yaxis.yaxis_mode == 'linear':
                where_x_has_same_sign_as_xaxis = np.where(curve.data_x * self.xaxis_sign > 0.)[0]
                runs_where_x_has_same_sign_as_xaxis = np.split(where_x_has_same_sign_as_xaxis, np.where(np.diff(where_x_has_same_sign_as_xaxis) != 1)[0] + 1)
                curve.points_x = [self.xaxis_sign * np.log10(self.xaxis_sign * curve.data_x[run]) for run in runs_where_x_has_same_sign_as_xaxis]
                curve.points_y = [curve.data_y[run].copy() for run in runs_where_x_has_same_sign_as_xaxis]
            elif yaxis.yaxis_mode == 'log':
                where_xy_have_same_sign_as_axes = np.where(np.logical_and(curve.data_x * self.xaxis_sign > 0., curve.data_y * yaxis.yaxis_sign > 0.))[0]
                runs_where_xy_have_same_sign_as_axes = np.split(where_xy_have_same_sign_as_axes, np.where(np.diff(where_xy_have_same_sign_as_axes) != 1)[0] + 1)
                curve.points_x = [self.xaxis_sign * np.log10(self.xaxis_sign * curve.data_x[run]) for run in runs_where_xy_have_same_sign_as_axes]
                curve.points_y = [yaxis.yaxis_sign * np.log10(yaxis.yaxis_sign * curve.data_y[run]) for run in runs_where_xy_have_same_sign_as_axes]

        self.refresh_plot()

    def grid(self, *args):
        if len(args) == 0:
            return self.grid_state
        elif args[0] in ('on', 'off'):
            self.grid_state = args[0]
            self.erase_plot()
            self.draw_plot()
        else:
            raise ValueError("invalid grid state specified; it must either be 'on' or 'off'")

    def xlabel(self, *args):
        if len(args) == 0:
            return self.xlabel_value
        else:
            self.xlabel_value = args[0]
            self.erase_plot()
            self.draw_plot()

    def ylabel(self, *args, **kwargs):
        yaxis = kwargs.get('yaxis', 'left')
        if yaxis not in self.yaxes.keys():
            raise ValueError("specified y-axis does not exist")

        if len(args) == 0:
            return self.yaxes[yaxis].ylabel_value
        else:
            self.yaxes[yaxis].ylabel_value = str(args[0])
            self.erase_plot()
            self.draw_plot()

    def xaxis(self, *args):
        if len(args) == 0:
            return self.xaxis_mode
        elif args[0] == 'linear':
            self.xaxis_mode = 'linear'
            self.xlimits_mode = 'auto'

            for curve_name in self.curves.keys():
                curve = self.curves[curve_name]
                yaxis = self.yaxes[curve.yaxis]
                if yaxis.yaxis_mode == 'linear':
                    curve.points_x = [curve.data_x.copy()]
                    curve.points_y = [curve.data_y.copy()]
                elif yaxis.yaxis_mode == 'log':
                    where_y_has_same_sign_as_yaxis = np.where(curve.data_y * yaxis.yaxis_sign > 0.)[0]
                    runs_where_y_has_same_sign_as_yaxis = np.split(where_y_has_same_sign_as_yaxis, np.where(np.diff(where_y_has_same_sign_as_yaxis) != 1)[0] + 1)
                    curve.points_x = [curve.data_x[run].copy() for run in runs_where_y_has_same_sign_as_yaxis]
                    curve.points_y = [yaxis.yaxis_sign * np.log10(yaxis.yaxis_sign * curve.data_y[run]) for run in runs_where_y_has_same_sign_as_yaxis]
            self.refresh_plot()
        elif args[0] == 'log':
            self.xaxis_mode = 'log'
            pos_x_values = 0
            total_x_values = 0
            for curve_name in self.curves.keys():
                pos_x_values += len(np.where(self.curves[curve_name].data_x > 0.)[0])
                total_x_values += len(self.curves[curve_name].data_x)
            self.xaxis_sign = 1. if pos_x_values >= total_x_values // 2 else -1.
            self.xlimits_mode = 'auto'

            for curve_name in self.curves.keys():
                curve = self.curves[curve_name]
                yaxis = self.yaxes[curve.yaxis]
                if yaxis.yaxis_mode == 'linear':
                    where_x_has_same_sign_as_xaxis = np.where(curve.data_x * self.xaxis_sign > 0.)[0]
                    runs_where_x_has_same_sign_as_xaxis = np.split(where_x_has_same_sign_as_xaxis, np.where(np.diff(where_x_has_same_sign_as_xaxis) != 1)[0] + 1)
                    curve.points_x = [self.xaxis_sign * np.log10(self.xaxis_sign * curve.data_x[run]) for run in runs_where_x_has_same_sign_as_xaxis]
                    curve.points_y = [curve.data_y[run].copy() for run in runs_where_x_has_same_sign_as_xaxis]
                elif yaxis.yaxis_mode == 'log':
                    where_xy_have_same_sign_as_axes = np.where(np.logical_and(curve.data_x * self.xaxis_sign > 0., curve.data_y * yaxis.yaxis_sign > 0.))[0]
                    runs_where_xy_have_same_sign_as_axes = np.split(where_xy_have_same_sign_as_axes, np.where(np.diff(where_xy_have_same_sign_as_axes) != 1)[0] + 1)
                    curve.points_x = [self.xaxis_sign * np.log10(self.xaxis_sign * curve.data_x[run]) for run in runs_where_xy_have_same_sign_as_axes]
                    curve.points_y = [yaxis.yaxis_sign * np.log10(yaxis.yaxis_sign * curve.data_y[run]) for run in runs_where_xy_have_same_sign_as_axes]
            self.refresh_plot()
        else:
            raise ValueError("invalid x-axis mode specified; it must either be 'linear' or 'log'")

    def yaxis(self, *args, **kwargs):
        yaxis = kwargs.get('yaxis', 'left')
        if yaxis not in self.yaxes.keys():
            raise ValueError("specified y-axis does not exist")

        if len(args) == 0:
            return self.yaxes[yaxis].yaxis_mode
        elif args[0] == 'linear':
            self.yaxes[yaxis].yaxis_mode = 'linear'
            self.yaxes[yaxis].ylimits_mode = 'auto'

            if self.xaxis_mode == 'linear':
                for curve_name in self.curves.keys():
                    if self.curves[curve_name].yaxis == yaxis:
                        self.curves[curve_name].points_x = [self.curves[curve_name].data_x.copy()]
                        self.curves[curve_name].points_y = [self.curves[curve_name].data_y.copy()]
            elif self.xaxis_mode == 'log':
                for curve_name in self.curves.keys():
                    if self.curves[curve_name].yaxis == yaxis:
                        where_x_has_same_sign_as_xaxis = np.where(self.curves[curve_name].data_x * self.xaxis_sign > 0.)[0]
                        runs_where_x_has_same_sign_as_xaxis = np.split(where_x_has_same_sign_as_xaxis, np.where(np.diff(where_x_has_same_sign_as_xaxis) != 1)[0] + 1)
                        self.curves[curve_name].points_x = [self.xaxis_sign * np.log10(self.xaxis_sign * self.curves[curve_name].data_x[run]) for run in runs_where_x_has_same_sign_as_xaxis]
                        self.curves[curve_name].points_y = [self.curves[curve_name].data_y[run].copy() for run in runs_where_x_has_same_sign_as_xaxis]
            self.refresh_plot()
        elif args[0] == 'log':
            self.yaxes[yaxis].yaxis_mode = 'log'
            pos_y_values = 0
            total_y_values = 0
            for curve_name in self.curves.keys():
                if self.curves[curve_name].yaxis == yaxis:
                    pos_y_values += len(np.where(self.curves[curve_name].data_y > 0.)[0])
                    total_y_values += len(self.curves[curve_name].data_y)
            self.yaxes[yaxis].yaxis_sign = 1. if pos_y_values >= total_y_values // 2 else -1.
            self.yaxes[yaxis].ylimits_mode = 'auto'

            if self.xaxis_mode == 'linear':
                for curve_name in self.curves.keys():
                    if self.curves[curve_name].yaxis == yaxis:
                        where_y_has_same_sign_as_yaxis = np.where(self.curves[curve_name].data_y * self.yaxes[yaxis].yaxis_sign > 0.)[0]
                        runs_where_y_has_same_sign_as_yaxis = np.split(where_y_has_same_sign_as_yaxis, np.where(np.diff(where_y_has_same_sign_as_yaxis) != 1)[0] + 1)
                        self.curves[curve_name].points_x = [self.curves[curve_name].data_x[run].copy() for run in runs_where_y_has_same_sign_as_yaxis]
                        self.curves[curve_name].points_y = [self.yaxes[yaxis].yaxis_sign * np.log10(self.yaxes[yaxis].yaxis_sign * self.curves[curve_name].data_y[run]) for run in runs_where_y_has_same_sign_as_yaxis]
            elif self.xaxis_mode == 'log':
                for curve_name in self.curves.keys():
                    if self.curves[curve_name].yaxis == yaxis:
                        where_xy_have_same_sign_as_axes = np.where(np.logical_and(self.curves[curve_name].data_x * self.xaxis_sign > 0., self.curves[curve_name].data_y * self.yaxes[yaxis].yaxis_sign > 0.))[0]
                        runs_where_xy_have_same_sign_as_axes = np.split(where_xy_have_same_sign_as_axes, np.where(np.diff(where_xy_have_same_sign_as_axes) != 1)[0] + 1)
                        self.curves[curve_name].points_x = [self.xaxis_sign * np.log10(self.xaxis_sign * self.curves[curve_name].data_x[run]) for run in runs_where_xy_have_same_sign_as_axes]
                        self.curves[curve_name].points_y = [self.yaxes[yaxis].yaxis_sign * np.log10(self.yaxes[yaxis].yaxis_sign * self.curves[curve_name].data_y[run]) for run in runs_where_xy_have_same_sign_as_axes]
            self.refresh_plot()
        else:
            raise ValueError("invalid y-axis mode specified; it must either be 'linear' or 'log'")

    def xlimits(self, *args):
        if len(args) == 0:
            if self.xaxis_mode == 'linear':
                return [self.xlim[0], self.xlim[1]]
            elif self.xaxis_mode == 'log':
                return [self.xaxis_sign * math.pow(10., self.xaxis_sign * self.xlim[0]), self.xaxis_sign * math.pow(10., self.xaxis_sign * self.xlim[1])]
        elif args[0] in ('auto', 'tight'):
            self.xlimits_mode = args[0]
        elif type(args[0]) is list:
            if len(args[0]) == 2:
                args[0][0] = float(args[0][0])
                args[0][1] = float(args[0][1])
                if args[0][0] == args[0][1]:
                    raise ValueError('specified lower limit and upper limit were not distinct')
                else:
                    if self.xaxis_mode == 'linear':
                        self.xlimits_mode = 'manual'
                        if args[0][0] < args[0][1]:
                            self.xlim[0] = args[0][0]
                            self.xlim[1] = args[0][1]
                        else:
                            self.xlim[0] = args[0][1]
                            self.xlim[1] = args[0][0]
                    elif self.xaxis_mode == 'log':
                        if args[0][0] * args[0][1] < 0.:
                            raise ValueError('for a logarithmic axis, both limits must have the same sign')
                        if (args[0][0] * args[0][1] == 0.) or (args[0][0] * args[0][1] == -0.):
                            raise ValueError('for a logarithmic axis, neither limit can be zero')
                        self.xlimits_mode = 'manual'
                        if self.xaxis_sign * args[0][0] < 0.:
                            self.xaxis_sign = -self.xaxis_sign
                            for curve_name in self.curves.keys():
                                curve = self.curves[curve_name]
                                yaxis = self.yaxes[curve.yaxis]
                                if yaxis.yaxis_mode == 'linear':
                                    where_x_has_same_sign_as_xaxis = np.where(curve.data_x * self.xaxis_sign > 0.)[0]
                                    runs_where_x_has_same_sign_as_xaxis = np.split(where_x_has_same_sign_as_xaxis, np.where(np.diff(where_x_has_same_sign_as_xaxis) != 1)[0] + 1)
                                    curve.points_x = [self.xaxis_sign * np.log10(self.xaxis_sign * curve.data_x[run]) for run in runs_where_x_has_same_sign_as_xaxis]
                                    curve.points_y = [curve.data_y[run].copy() for run in runs_where_x_has_same_sign_as_xaxis]
                                elif yaxis.yaxis_mode == 'log':
                                    where_xy_have_same_sign_as_axes = np.where(np.logical_and(curve.data_x * self.xaxis_sign > 0., curve.data_y * yaxis.yaxis_sign > 0.))[0]
                                    runs_where_xy_have_same_sign_as_axes = np.split(where_xy_have_same_sign_as_axes, np.where(np.diff(where_xy_have_same_sign_as_axes) != 1)[0] + 1)
                                    curve.points_x = [self.xaxis_sign * np.log10(self.xaxis_sign * curve.data_x[run]) for run in runs_where_xy_have_same_sign_as_axes]
                                    curve.points_y = [yaxis.yaxis_sign * np.log10(yaxis.yaxis_sign * curve.data_y[run]) for run in runs_where_xy_have_same_sign_as_axes]
                        if args[0][0] < args[0][1]:
                            self.xlim[0] = self.xaxis_sign * math.log10(self.xaxis_sign * args[0][0])
                            self.xlim[1] = self.xaxis_sign * math.log10(self.xaxis_sign * args[0][1])
                        else:
                            self.xlim[0] = self.xaxis_sign * math.log10(self.xaxis_sign * args[0][1])
                            self.xlim[1] = self.xaxis_sign * math.log10(self.xaxis_sign * args[0][0])
            elif len(args[0]) < 2:
                raise IndexError('did not specify both a lower and an upper limit for the x-axis')
            else:
                raise IndexError('more than two limits were specified for the x-axis')
        else:
            raise ValueError("invalid x-limits specification; it must be 'auto', 'tight', or a list of limits")
        self.refresh_plot()

    def ylimits(self, *args, **kwargs):
        yaxis = kwargs.get('yaxis', 'left')
        if yaxis not in self.yaxes.keys():
            raise ValueError("specified y-axis does not exist")

        if len(args) == 0:
            if self.yaxes[yaxis].yaxis_mode == 'linear':
                return [self.yaxes[yaxis].ylim[0], self.yaxes[yaxis].ylim[1]]
            elif self.yaxes[yaxis].yaxis_mode == 'log':
                return [self.yaxes[yaxis].yaxis_sign * math.pow(10., self.yaxes[yaxis].yaxis_sign * self.yaxes[yaxis].ylim[0]), self.yaxes[yaxis].yaxis_sign * math.pow(10., self.yaxes[yaxis].yaxis_sign * self.yaxes[yaxis].ylim[1])]
        elif args[0] in ('auto', 'tight'):
            self.yaxes[yaxis].ylimits_mode = args[0]
        elif type(args[0]) is list:
            if len(args[0]) == 2:
                args[0][0] = float(args[0][0])
                args[0][1] = float(args[0][1])
                if args[0][0] == args[0][1]:
                    raise ValueError('specified lower limit and upper limit were not distinct')
                else:
                    if self.yaxes[yaxis].yaxis_mode == 'linear':
                        self.yaxes[yaxis].ylimits_mode = 'manual'
                        if args[0][0] < args[0][1]:
                            self.yaxes[yaxis].ylim[0] = args[0][0]
                            self.yaxes[yaxis].ylim[1] = args[0][1]
                        else:
                            self.yaxes[yaxis].ylim[0] = args[0][1]
                            self.yaxes[yaxis].ylim[1] = args[0][0]
                    elif self.yaxes[yaxis].yaxis_mode == 'log':
                        if args[0][0] * args[0][1] < 0.:
                            raise ValueError('for a logarithmic axis, both limits must have the same sign')
                        if (args[0][0] * args[0][1] == 0.) or (args[0][0] * args[0][1] == -0.):
                            raise ValueError('for a logarithmic axis, neither limit can be zero')
                        self.yaxes[yaxis].ylimits_mode = 'manual'
                        if self.yaxes[yaxis].yaxis_sign * args[0][0] < 0.:
                            self.yaxes[yaxis].yaxis_sign = -self.yaxes[yaxis].yaxis_sign
                            if self.xaxis_mode == 'linear':
                                for curve_name in self.curves.keys():
                                    if self.curves[curve_name].yaxis == yaxis:
                                        where_y_has_same_sign_as_yaxis = np.where(self.curves[curve_name].data_y * self.yaxes[yaxis].yaxis_sign > 0.)[0]
                                        runs_where_y_has_same_sign_as_yaxis = np.split(where_y_has_same_sign_as_yaxis, np.where(np.diff(where_y_has_same_sign_as_yaxis) != 1)[0] + 1)
                                        self.curves[curve_name].points_x = [self.curves[curve_name].data_x[run].copy() for run in runs_where_y_has_same_sign_as_yaxis]
                                        self.curves[curve_name].points_y = [self.yaxes[yaxis].yaxis_sign * np.log10(self.yaxes[yaxis].yaxis_sign * self.curves[curve_name].data_y[run]) for run in runs_where_y_has_same_sign_as_yaxis]
                            elif self.xaxis_mode == 'log':
                                for curve_name in self.curves.keys():
                                    if self.curves[curve_name].yaxis == yaxis:
                                        where_xy_have_same_sign_as_axes = np.where(np.logical_and(self.curves[curve_name].data_x * self.xaxis_sign > 0., self.curves[curve_name].data_y * self.yaxes[yaxis].yaxis_sign > 0.))[0]
                                        runs_where_xy_have_same_sign_as_axes = np.split(where_xy_have_same_sign_as_axes, np.where(np.diff(where_xy_have_same_sign_as_axes) != 1)[0] + 1)
                                        self.curves[curve_name].points_x = [self.xaxis_sign * np.log10(self.xaxis_sign * self.curves[curve_name].data_x[run]) for run in runs_where_xy_have_same_sign_as_axes]
                                        self.curves[curve_name].points_y = [self.yaxes[yaxis].yaxis_sign * np.log10(self.yaxes[yaxis].yaxis_sign * self.curves[curve_name].data_y[run]) for run in runs_where_xy_have_same_sign_as_axes]
                        if args[0][0] < args[0][1]:
                            self.yaxes[yaxis].ylim[0] = self.yaxes[yaxis].yaxis_sign * math.log10(self.yaxes[yaxis].yaxis_sign * args[0][0])
                            self.yaxes[yaxis].ylim[1] = self.yaxes[yaxis].yaxis_sign * math.log10(self.yaxes[yaxis].yaxis_sign * args[0][1])
                        else:
                            self.yaxes[yaxis].ylim[0] = self.yaxes[yaxis].yaxis_sign * math.log10(self.yaxes[yaxis].yaxis_sign * args[0][1])
                            self.yaxes[yaxis].ylim[1] = self.yaxes[yaxis].yaxis_sign * math.log10(self.yaxes[yaxis].yaxis_sign * args[0][0])
            elif len(args[0]) < 2:
                raise IndexError('did not specify both a lower and an upper limit for the y-axis')
            else:
                raise IndexError('more than two limits were specified for the y-axis')
        else:
            raise ValueError("invalid y-limits specification; it must be 'auto', 'tight', or a list of limits")
        self.refresh_plot()

    def svg(self, filename):
        self.svg_backend()

        self.svg_file = codecs.open(filename, encoding = 'utf-8', mode = 'w')
        self.svg_file.write(u'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width!s}px" height="{height!s}px" viewBox="0 0 {width!s} {height!s}">\n'.format(width = self.canvas_width, height = self.canvas_height))
        self.begin_group()
        self.draw_plot()
        self.end_group()
        self.svg_file.write(u'</svg>\n')
        self.svg_file.close()
        self.svg_file = None

        self.tk_backend()

    def zoom_to_fit(self, **kwargs):
        mode = kwargs.get('mode', 'auto')
        if mode not in ('auto', 'tight'):
            raise ValueError("if specified, mode must be 'auto' or 'tight'")

        yaxis = kwargs.get('yaxis', 'all')
        if (yaxis != 'all') and (yaxis not in self.yaxes.keys()):
            raise ValueError('specified y-axis does not exist')

        self.xlimits_mode = mode

        if yaxis == 'all':
            for yaxis in self.yaxes.keys():
                self.yaxes[yaxis].ylimits_mode = mode
        else:
            self.yaxes[yaxis].ylimits_mode = mode

        self.refresh_plot()

    def zoom_in(self, **kwargs):
        factor = kwargs.get('factor', math.sqrt(2))

        yaxis = kwargs.get('yaxis', 'all')
        if (yaxis != 'all') and (yaxis not in self.yaxes.keys()):
            raise ValueError('specified y-axis does not exist')

        cx = kwargs.get('cx', 0.5 * (self.axes_left + self.axes_right))
        cy = kwargs.get('cy', 0.5 * (self.axes_top + self.axes_bottom))

        x = self.from_canvas_x(cx)
        self.xlimits_mode = 'manual'
        self.xlim[0] = x - 0.5 * self.xrange / factor
        self.xlim[1] = x + 0.5 * self.xrange / factor

        if yaxis == 'all':
            for yaxis in self.yaxes.keys():
                y = self.from_canvas_y(cy, yaxis)
                self.yaxes[yaxis].ylimits_mode = 'manual'
                self.yaxes[yaxis].ylim[0] = y - 0.5 * self.yaxes[yaxis].yrange / factor
                self.yaxes[yaxis].ylim[1] = y + 0.5 * self.yaxes[yaxis].yrange / factor
        else:
            y = self.from_canvas_y(cy, yaxis)
            self.yaxes[yaxis].ylimits_mode = 'manual'
            self.yaxes[yaxis].ylim[0] = y - 0.5 * self.yaxes[yaxis].yrange / factor
            self.yaxes[yaxis].ylim[1] = y + 0.5 * self.yaxes[yaxis].yrange / factor

        self.refresh_plot()

    def zoom_in_x(self, **kwargs):
        factor = kwargs.get('factor', math.sqrt(2))

        cx = kwargs.get('cx', 0.5 * (self.axes_left + self.axes_right))

        x = self.from_canvas_x(cx)
        self.xlimits_mode = 'manual'
        self.xlim[0] = x - 0.5 * self.xrange / factor
        self.xlim[1] = x + 0.5 * self.xrange / factor

        self.refresh_plot()

    def zoom_in_y(self, **kwargs):
        factor = kwargs.get('factor', math.sqrt(2))

        yaxis = kwargs.get('yaxis', 'all')
        if (yaxis != 'all') and (yaxis not in self.yaxes.keys()):
            raise ValueError('specified y-axis does not exist')

        cy = kwargs.get('cy', 0.5 * (self.axes_top + self.axes_bottom))

        if yaxis == 'all':
            for yaxis in self.yaxes.keys():
                y = self.from_canvas_y(cy, yaxis)
                self.yaxes[yaxis].ylimits_mode = 'manual'
                self.yaxes[yaxis].ylim[0] = y - 0.5 * self.yaxes[yaxis].yrange / factor
                self.yaxes[yaxis].ylim[1] = y + 0.5 * self.yaxes[yaxis].yrange / factor
        else:
            y = self.from_canvas_y(cy, yaxis)
            self.yaxes[yaxis].ylimits_mode = 'manual'
            self.yaxes[yaxis].ylim[0] = y - 0.5 * self.yaxes[yaxis].yrange / factor
            self.yaxes[yaxis].ylim[1] = y + 0.5 * self.yaxes[yaxis].yrange / factor

        self.refresh_plot()

    def zoom_out(self, **kwargs):
        factor = kwargs.get('factor', math.sqrt(2))

        yaxis = kwargs.get('yaxis', 'all')
        if (yaxis != 'all') and (yaxis not in self.yaxes.keys()):
            raise ValueError('specified y-axis does not exist')

        cx = kwargs.get('cx', 0.5 * (self.axes_left + self.axes_right))
        cy = kwargs.get('cy', 0.5 * (self.axes_top + self.axes_bottom))

        x = self.from_canvas_x(cx)
        self.xlimits_mode = 'manual'
        self.xlim[0] = x - 0.5 * self.xrange * factor
        self.xlim[1] = x + 0.5 * self.xrange * factor

        if yaxis == 'all':
            for yaxis in self.yaxes.keys():
                y = self.from_canvas_y(cy, yaxis)
                self.yaxes[yaxis].ylimits_mode = 'manual'
                self.yaxes[yaxis].ylim[0] = y - 0.5 * self.yaxes[yaxis].yrange * factor
                self.yaxes[yaxis].ylim[1] = y + 0.5 * self.yaxes[yaxis].yrange * factor
        else:
            y = self.from_canvas_y(cy, yaxis)
            self.yaxes[yaxis].ylimits_mode = 'manual'
            self.yaxes[yaxis].ylim[0] = y - 0.5 * self.yaxes[yaxis].yrange * factor
            self.yaxes[yaxis].ylim[1] = y + 0.5 * self.yaxes[yaxis].yrange * factor

        self.refresh_plot()

    def zoom_out_x(self, **kwargs):
        factor = kwargs.get('factor', math.sqrt(2))

        cx = kwargs.get('cx', 0.5 * (self.axes_left + self.axes_right))

        x = self.from_canvas_x(cx)
        self.xlimits_mode = 'manual'
        self.xlim[0] = x - 0.5 * self.xrange * factor
        self.xlim[1] = x + 0.5 * self.xrange * factor

        self.refresh_plot()

    def zoom_out_y(self, **kwargs):
        factor = kwargs.get('factor', math.sqrt(2))

        yaxis = kwargs.get('yaxis', 'all')
        if (yaxis != 'all') and (yaxis not in self.yaxes.keys()):
            raise ValueError('specified y-axis does not exist')

        cy = kwargs.get('cy', 0.5 * (self.axes_top + self.axes_bottom))

        if yaxis == 'all':
            for yaxis in self.yaxes.keys():
                y = self.from_canvas_y(cy, yaxis)
                self.yaxes[yaxis].ylimits_mode = 'manual'
                self.yaxes[yaxis].ylim[0] = y - 0.5 * self.yaxes[yaxis].yrange * factor
                self.yaxes[yaxis].ylim[1] = y + 0.5 * self.yaxes[yaxis].yrange * factor
        else:
            y = self.from_canvas_y(cy, yaxis)
            self.yaxes[yaxis].ylimits_mode = 'manual'
            self.yaxes[yaxis].ylim[0] = y - 0.5 * self.yaxes[yaxis].yrange * factor
            self.yaxes[yaxis].ylim[1] = y + 0.5 * self.yaxes[yaxis].yrange * factor

        self.refresh_plot()

    def zoom_rect(self, *args, **kwargs):
        left = kwargs.get('left', self.axes_left)
        right = kwargs.get('right', self.axes_right)
        top = kwargs.get('top', self.axes_top)
        bottom = kwargs.get('bottom', self.axes_bottom)

        yaxis = kwargs.get('yaxis', 'all')
        if (yaxis != 'all') and (yaxis not in self.yaxes.keys()):
            raise ValueError('specified y-axis does not exist')

        if len(args) == 1:
            if (type(args[0]) is list) and (len(args[0]) == 4):
                left = float(args[0][0])
                right = float(args[0][2])
                top = float(args[0][1])
                bottom = float(args[0][3])
            else:
                raise ValueError('if specified, the optional argument must be a four-element list specifying the left, top, right, and bottom coordinates of the zoom rectangle')
        elif len(args) > 1:
            raise IndexError('too many arguments supplied to zoom_rect')

        if (left < right) and (top < bottom):
            self.xlimits_mode = 'manual'
            self.xlim[0], self.xlim[1] = self.from_canvas_x(left), self.from_canvas_x(right)

            if yaxis == 'all':
                for yaxis in self.yaxes.keys():
                    self.yaxes[yaxis].ylimits_mode = 'manual'
                    self.yaxes[yaxis].ylim[0], self.yaxes[yaxis].ylim[1] = self.from_canvas_y(bottom, yaxis), self.from_canvas_y(top, yaxis)
            else:
                self.yaxes[yaxis].ylimits_mode = 'manual'
                self.yaxes[yaxis].ylim[0], self.yaxes[yaxis].ylim[1] = self.from_canvas_y(bottom, yaxis), self.from_canvas_y(top, yaxis)

            self.refresh_plot()

    def pan_left(self, **kwargs):
        fraction = kwargs.get('fraction', 0.1)

        self.xlimits_mode = 'manual'
        self.xlim[0] -= fraction * self.xrange
        self.xlim[1] -= fraction * self.xrange

        self.refresh_plot()

    def pan_right(self, **kwargs):
        fraction = kwargs.get('fraction', 0.1)

        self.xlimits_mode = 'manual'
        self.xlim[0] += fraction * self.xrange
        self.xlim[1] += fraction * self.xrange

        self.refresh_plot()

    def pan_up(self, **kwargs):
        fraction = kwargs.get('fraction', 0.1)

        yaxis = kwargs.get('yaxis', 'all')
        if (yaxis != 'all') and (yaxis not in self.yaxes.keys()):
            raise ValueError('specified y-axis does not exist')

        if yaxis == 'all':
            for yaxis in self.yaxes.keys():
                self.yaxes[yaxis].ylimits_mode = 'manual'
                self.yaxes[yaxis].ylim[0] += fraction * self.yaxes[yaxis].yrange
                self.yaxes[yaxis].ylim[1] += fraction * self.yaxes[yaxis].yrange
        else:
            self.yaxes[yaxis].ylimits_mode = 'manual'
            self.yaxes[yaxis].ylim[0] += fraction * self.yaxes[yaxis].yrange
            self.yaxes[yaxis].ylim[1] += fraction * self.yaxes[yaxis].yrange

        self.refresh_plot()

    def pan_down(self, **kwargs):
        fraction = kwargs.get('fraction', 0.1)

        yaxis = kwargs.get('yaxis', 'all')
        if (yaxis != 'all') and (yaxis not in self.yaxes.keys()):
            raise ValueError('specified y-axis does not exist')

        if yaxis == 'all':
            for yaxis in self.yaxes.keys():
                self.yaxes[yaxis].ylimits_mode = 'manual'
                self.yaxes[yaxis].ylim[0] -= fraction * self.yaxes[yaxis].yrange
                self.yaxes[yaxis].ylim[1] -= fraction * self.yaxes[yaxis].yrange
        else:
            self.yaxes[yaxis].ylimits_mode = 'manual'
            self.yaxes[yaxis].ylim[0] -= fraction * self.yaxes[yaxis].yrange
            self.yaxes[yaxis].ylim[1] -= fraction * self.yaxes[yaxis].yrange

        self.refresh_plot()

    def pan(self, **kwargs):
        dx = kwargs.get('dx', 0.)
        dy = kwargs.get('dy', 0.)

        yaxis = kwargs.get('yaxis', 'all')
        if (yaxis != 'all') and (yaxis not in self.yaxes.keys()):
            raise ValueError('specified y-axis does not exist')

        if (dx != 0.) or (dy != 0.):
            self.xlimits_mode = 'manual'
            self.xlim[0] -= dx * self.x_epsilon
            self.xlim[1] -= dx * self.x_epsilon

            if yaxis == 'all':
                for yaxis in self.yaxes.keys():
                    self.yaxes[yaxis].ylimits_mode = 'manual'
                    self.yaxes[yaxis].ylim[0] += dy * self.yaxes[yaxis].y_epsilon
                    self.yaxes[yaxis].ylim[1] += dy * self.yaxes[yaxis].y_epsilon
            else:
                self.yaxes[yaxis].ylimits_mode = 'manual'
                self.yaxes[yaxis].ylim[0] += dy * self.yaxes[yaxis].y_epsilon
                self.yaxes[yaxis].ylim[1] += dy * self.yaxes[yaxis].y_epsilon

            self.refresh_plot()

    def delete_curve(self, name):
        if name in self.curves:
            del(self.curves[name])
        else:
            raise NameError('no curve exists with name = {0!r}'.format(name))

        self.refresh_plot()

    def configure_curve(self, name, **kwargs):
        style = kwargs.get('style', '')

        if name in self.curves:
            marker_color = kwargs.get('marker_color', self.curves[name].marker_color)
            marker = kwargs.get('marker', self.curves[name].marker)
            curve_color = kwargs.get('curve_color', self.curves[name].curve_color)
            curve_style = kwargs.get('curve_style', self.curves[name].curve_style)
            if style == '':
                self.curves[name].marker_color = marker_color
                self.curves[name].marker = marker
                self.curves[name].curve_color = curve_color
                self.curves[name].curve_style = curve_style
            else:
                [self.curves[name].marker_color, self.curves[name].marker, self.curves[name].curve_color, self.curves[name].curve_style] = self.parse_style(style)
        else:
            raise NameError('no curve exists with name = {0!r}'.format(name))

        self.refresh_plot()

    def bindings(self):
        self.key_bindings()
        self.mouse_bindings()

    def key_bindings(self):
        self.canvas.bind('<Up>', lambda event: self.pan_up())
        self.canvas.bind('<Down>', lambda event: self.pan_down())
        self.canvas.bind('<Left>', lambda event: self.pan_left())
        self.canvas.bind('<Right>', lambda event: self.pan_right())
        self.canvas.bind('<Control-Up>', lambda event: self.pan_up(fraction = 0.5))
        self.canvas.bind('<Control-Down>', lambda event: self.pan_down(fraction = 0.5))
        self.canvas.bind('<Control-Left>', lambda event: self.pan_left(fraction = 0.5))
        self.canvas.bind('<Control-Right>', lambda event: self.pan_right(fraction = 0.5))
        self.canvas.bind('<Shift-Up>', lambda event: self.pan_up(fraction = 1. / self.axes_height))
        self.canvas.bind('<Shift-Down>', lambda event: self.pan_down(fraction = 1. / self.axes_height))
        self.canvas.bind('<Shift-Left>', lambda event: self.pan_left(fraction = 1. / self.axes_width))
        self.canvas.bind('<Shift-Right>', lambda event: self.pan_right(fraction = 1. / self.axes_width))
        self.canvas.bind('=', lambda event: self.zoom_in())
        self.canvas.bind('-', lambda event: self.zoom_out())
        self.canvas.bind('<Control-equal>', lambda event: self.zoom_in(factor = 2.))
        self.canvas.bind('<Control-minus>', lambda event: self.zoom_out(factor = 2.))
        self.canvas.bind('+', lambda event: self.zoom_in(factor = math.sqrt(math.sqrt(2.))))
        self.canvas.bind('_', lambda event: self.zoom_out(factor = math.sqrt(math.sqrt(2.))))
        self.canvas.bind('h', lambda event: self.zoom_to_fit())
        self.canvas.bind('<Home>', lambda event: self.zoom_to_fit())
        self.canvas.bind('g', lambda event: self.grid('off') if self.grid() == 'on' else self.grid('on'))
        self.canvas.bind('x', lambda event: self.xaxis('log') if self.xaxis() == 'linear' else self.xaxis('linear'))
        self.canvas.bind('y', lambda event: self.yaxis('log') if self.yaxis() == 'linear' else self.yaxis('linear'))
        self.canvas.bind('l', lambda event: self.yaxis('log') if self.yaxis() == 'linear' else self.yaxis('linear'))
        self.canvas.bind('r', lambda event: self.yaxis('log', side = 'right') if self.yaxis(side = 'right') == 'linear' else self.yaxis('linear', side = 'right'))

    def mouse_bindings(self):
        self.marker_color = tk.StringVar()
        self.marker_color.set('b')
        self.marker = tk.StringVar()
        self.marker.set('')
        self.curve_color = tk.StringVar()
        self.curve_color.set('b')
        self.curve_style = tk.StringVar()
        self.marker.set('')
        self.curve_name = ''
        self.curve_menu = tk.Menu(self.canvas, tearoff = 0)
        marker_menu = tk.Menu(self.curve_menu, tearoff = 0)
        for [val, name] in self.marker_names:
            marker_menu.add_radiobutton(label = name, variable = self.marker, value = val, command = self.configure_curve_callback)
        self.curve_menu.add_cascade(label = 'Marker', menu = marker_menu)
        marker_color_menu = tk.Menu(self.curve_menu, tearoff = 0)
        for [val, name] in self.color_names:
            marker_color_menu.add_radiobutton(label = name, variable = self.marker_color, value = val, command = self.configure_curve_callback)
        self.curve_menu.add_cascade(label = 'Marker color', menu = marker_color_menu)
        curve_style_menu = tk.Menu(self.curve_menu, tearoff = 0)
        for [val, name] in self.linestyle_names:
            curve_style_menu.add_radiobutton(label = name, variable = self.curve_style, value = val, command = self.configure_curve_callback)
        self.curve_menu.add_cascade(label = 'Curve style', menu = curve_style_menu)
        curve_color_menu = tk.Menu(self.curve_menu, tearoff = 0)
        for [val, name] in self.color_names:
            curve_color_menu.add_radiobutton(label = name, variable = self.curve_color, value = val, command = self.configure_curve_callback)
        self.curve_menu.add_cascade(label = 'Curve color', menu = curve_color_menu)
        self.curve_menu.add_separator()
        self.curve_menu.add_command(label = 'Delete', command = lambda: self.delete_curve(self.curve_name))

        windowing_system = self.root.tk.call('tk', 'windowingsystem')
        self.arrow = 'arrow'
#        if windowing_system=='x11':
#            self.zoom = ('@cursors/zoom.xbm', 'cursors/zoom.xbm', 'black', 'white')
#            self.zoomin = ('@cursors/zoomin.xbm', 'cursors/zoommask.xbm', 'black', 'white')
#            self.zoomout = ('@cursors/zoomout.xbm', 'cursors/zoommask.xbm', 'black', 'white')
#            self.openhand = ('@cursors/openhand.xbm', 'cursors/openhandmask.xbm', 'black', 'white')
#            self.closedhand = ('@cursors/closedhand.xbm', 'cursors/closedhandmask.xbm', 'black', 'white')
#        elif windowing_system=='win32':
#            self.zoom = '@cursors/zoom.cur'
#            self.zoomin = '@cursors/zoomin.cur'
#            self.zoomout = '@cursors/zoomout.cur'
#            self.openhand = '@cursors/openhand.cur'
#            self.closedhand = '@cursors/closedhand.cur'
#        elif windowing_system=='aqua':
#            self.zoom = 'arrow'
#            self.zoomin = 'arrow'
#            self.zoomout = 'arrow'
#            self.openhand = 'openhand'
#            self.closedhand = 'closedhand'
#        else:
        self.zoom = 'arrow'
        self.zoomin = 'arrow'
        self.zoomout = 'arrow'
        self.openhand = 'arrow'
        self.closedhand = 'arrow'
        self.canvas.bind('<Control-Button-1>', self.curve_context_menu)
        self.canvas.bind('<Button-3>', self.curve_context_menu)
        self.canvas.bind('<Escape>', self.cancel_mouse_zoom_pan)
        self.canvas.bind('z', self.setup_mouse_zoom)
        self.canvas.bind('b', self.setup_mouse_box_zoom)
        self.canvas.bind('p', self.setup_mouse_pan)

    def curve_context_menu(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if (x > self.axes_left) and (x < self.axes_right) and (y > self.axes_top) and (y < self.axes_bottom):
            items = self.canvas.find_overlapping(x - 2., y - 2., x + 2., y + 2.)
            name = ''
            for item in items:
                tags = self.canvas.gettags(item)
                if (tags != ()) and (tags[0] != 'current'):
                    name = tags[0]
            if name != '':
                if name in self.curves:
                    self.curve_name = name
                    self.marker_color.set(self.curves[name].marker_color)
                    self.marker.set(self.curves[name].marker)
                    self.curve_color.set(self.curves[name].curve_color)
                    self.curve_style.set(self.curves[name].curve_style)
                else:
                    raise NameError('no curve exists with name = {0!r}'.format(name))
                self.curve_menu.post(event.x_root, event.y_root)

    def configure_curve_callback(self):
        marker = self.marker.get()
        if marker == ' ':
            marker = ''
        curve_style = self.curve_style.get()
        if curve_style == ' ':
            curve_style = ''
        if self.curve_name in self.curves:
            if (marker == '') and (curve_style == ''):
                self.delete_curve(self.curve_name)
            else:
                self.curves[self.curve_name].marker_color = self.marker_color.get()
                self.curves[self.curve_name].marker = marker
                self.curves[self.curve_name].curve_color = self.curve_color.get()
                self.curves[self.curve_name].curve_style = curve_style
        else:
            raise NameError('no curve exists with name = {0!r}'.format(name))
        self.refresh_plot()

    def cancel_mouse_zoom_pan(self, event):
        self.canvas.bind('<Button-1>', lambda event: None)
        self.canvas.bind('<Shift-Button-1>', lambda event: None)
        self.canvas.bind('<Shift_L>', lambda event: None)
        self.canvas.bind('<KeyRelease-Shift_L>', lambda event: None)
        self.canvas.bind('<B1-Motion>', lambda event: None)
        self.canvas.bind('<ButtonRelease-1>', lambda event: None)
        self.canvas.configure(cursor = self.arrow)

    def setup_mouse_zoom(self, event):
        self.canvas.bind('<Button-1>', self.mouse_zoom_in)
        self.canvas.bind('<Shift-Button-1>', self.mouse_zoom_out)
        self.canvas.bind('<Shift_L>', lambda event: self.canvas.configure(cursor = self.zoomout))
        self.canvas.bind('<KeyRelease-Shift_L>', lambda event: self.canvas.configure(cursor = self.zoomin))
        self.canvas.bind('<B1-Motion>', lambda event: None)
        self.canvas.bind('<ButtonRelease-1>', lambda event: None)
        self.canvas.configure(cursor = self.zoomin)

    def mouse_zoom_in(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if (x >= self.axes_left) and (x <= self.axes_right) and (y >= self.axes_top) and (y <= self.axes_bottom):
            self.zoom_in(cx = x, cy = y)

    def mouse_zoom_out(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if (x >= self.axes_left) and (x <= self.axes_right) and (y >= self.axes_top) and (y <= self.axes_bottom):
            self.zoom_out(cx = x, cy = y)

    def setup_mouse_box_zoom(self, event):
        self.canvas.bind('<Button-1>', self.start_mouse_box_zoom)
        self.canvas.bind('<Shift-Button-1>', lambda event: None)
        self.canvas.bind('<Shift_L>', lambda event: None)
        self.canvas.bind('<KeyRelease-Shift_L>', lambda event: None)
        self.canvas.bind('<B1-Motion>', lambda event: None)
        self.canvas.bind('<ButtonRelease-1>', lambda event: None)
        self.canvas.configure(cursor = self.zoom)

    def start_mouse_box_zoom(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if (x >= self.axes_left) and (x <= self.axes_right) and (y >= self.axes_top) and (y <= self.axes_bottom):
            self.x0 = x
            self.y0 = y
            self.canvas.create_rectangle([self.x0, self.y0, self.x0, self.y0], outline = self.axes_color, fill = '', dash = (1, 4), tags = 'zoombox')
            self.canvas.bind('<B1-Motion>', self.continue_mouse_box_zoom)
            self.canvas.bind('<ButtonRelease-1>', self.finish_mouse_box_zoom)

    def continue_mouse_box_zoom(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if x < self.axes_left:
            x = self.axes_left
        if x > self.axes_right:
            x = self.axes_right
        if y < self.axes_top:
            y = self.axes_top
        if y > self.axes_bottom:
            y = self.axes_bottom
        self.canvas.coords('zoombox', self.x0, self.y0, x, y)

    def finish_mouse_box_zoom(self, event):
        self.canvas.delete('zoombox')
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if x < self.axes_left:
            x = self.axes_left
        if x > self.axes_right:
            x = self.axes_right
        if y < self.axes_top:
            y = self.axes_top
        if y > self.axes_bottom:
            y = self.axes_bottom
        if x < self.x0:
            self.x0, x = x, self.x0
        if y < self.y0:
            self.y0, y = y, self.y0
        self.zoom_rect([self.x0, self.y0, x, y])
        self.canvas.bind('<B1-Motion>', lambda event: None)
        self.canvas.bind('<ButtonRelease-1>', lambda event: None)

    def setup_mouse_pan(self, event):
        self.canvas.bind('<Button-1>', self.start_mouse_pan)
        self.canvas.bind('<Shift-Button-1>', lambda event: None)
        self.canvas.bind('<Shift_L>', lambda event: None)
        self.canvas.bind('<KeyRelease-Shift_L>', lambda event: None)
        self.canvas.bind('<B1-Motion>', lambda event: None)
        self.canvas.bind('<ButtonRelease-1>', lambda event: None)
        self.canvas.configure(cursor = self.openhand)

    def start_mouse_pan(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        if (x >= self.axes_left) and (x <= self.axes_right) and (y >= self.axes_top) and (y <= self.axes_bottom):
            self.x0 = x
            self.y0 = y
            self.canvas.bind('<B1-Motion>', self.continue_mouse_pan)
            self.canvas.bind('<ButtonRelease-1>', self.finish_mouse_pan)
            self.canvas.configure(cursor = self.closedhand)

    def continue_mouse_pan(self, event):
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        self.pan(dx = x - self.x0, dy = y - self.y0)
        self.x0 = x
        self.y0 = y

    def finish_mouse_pan(self, event):
        self.canvas.bind('<B1-Motion>', lambda event: None)
        self.canvas.bind('<ButtonRelease-1>', lambda event: None)
        self.canvas.configure(cursor = self.openhand)

    def tk_backend(self):
        self.erase_plot = self.tk_erase_plot
        self.draw_rect = self.tk_draw_rect
        self.draw_oval = self.tk_draw_oval
        self.draw_line = self.tk_draw_line
        self.draw_text = self.tk_draw_text
        self.begin_group = self.tk_begin_group
        self.end_group = self.tk_end_group

    def tk_erase_plot(self):
        self.canvas.delete('all')

    def tk_draw_rect(self, **kwargs):
        coords = kwargs.get('coords', [])
        outline_color = kwargs.get('outline', '')
        fill_color = kwargs.get('fill', '')
        name = kwargs.get('name', '')
        
        item = self.canvas.create_rectangle(coords, outline = outline_color, fill = fill_color)
        if name != '':
            self.canvas.itemconfig(item, tags = name)

    def tk_draw_oval(self, **kwargs):
        coords = kwargs.get('coords', [])
        outline_color = kwargs.get('outline', '')
        fill_color = kwargs.get('fill', '')
        line_weight = kwargs.get('width', 1.)
        name = kwargs.get('name', '')

        item = self.canvas.create_oval(coords, outline = outline_color, fill = fill_color, width = line_weight)
        if name != '':
            self.canvas.itemconfig(item, tags = name)

    def tk_draw_line(self, **kwargs):
        coords = kwargs.get('coords', [])
        fill = kwargs.get('fill', '')
        line_style = kwargs.get('dash', ())
        line_weight = kwargs.get('width', 1.)
        name = kwargs.get('name', '')

        item = self.canvas.create_line(coords, fill = fill, dash = line_style, width = line_weight)
        if name != '':
            self.canvas.itemconfig(item, tags = name)

    def tk_draw_text(self, **kwargs):
        text = kwargs.get('text', '')
        coords = kwargs.get('coords', [])
        fill = kwargs.get('fill', '')
        font = kwargs.get('font', (self.label_font, self.label_fontsize))
        anchor = kwargs.get('anchor', 'center')
        justify = kwargs.get('justify', 'center')
        name = kwargs.get('name', '')

        if text != '':
            item = self.canvas.create_text(coords, text = text, font = font, fill = fill, anchor = anchor, justify = justify)
            if name != '':
                self.canvas.itemconfig(item, tags = name)

    def tk_begin_group(self, **kwargs):
        pass

    def tk_end_group(self, **kwargs):
        pass

    def svg_backend(self):
        self.erase_plot = self.svg_erase_plot
        self.draw_rect = self.svg_draw_rect
        self.draw_oval = self.svg_draw_oval
        self.draw_line = self.svg_draw_line
        self.draw_text = self.svg_draw_text
        self.begin_group = self.svg_begin_group
        self.end_group = self.svg_end_group

    def svg_erase_plot(self):
        pass

    def svg_draw_rect(self, **kwargs):
        coords = kwargs.get('coords', [])
        outline_color = kwargs.get('outline', 'none')
        fill_color = kwargs.get('fill', 'none')
        name = kwargs.get('name', '')

        self.svg_file.write(u'{indent}<rect x="{x!s}" y="{y!s}" width="{width!s}" height="{height!s}" stroke="{outline_color}" fill="{fill_color}"/>\n'.format(indent = '    ' * self.svg_indent_level, x = coords[0], y = coords[1], width = coords[2] - coords[0], height = coords[3] - coords[1], outline_color = outline_color, fill_color = fill_color))

    def svg_draw_oval(self, **kwargs):
        coords = kwargs.get('coords', [])
        outline_color = kwargs.get('outline', '')
        fill_color = kwargs.get('fill', '')
        line_weight = kwargs.get('width', 1.)
        name = kwargs.get('name', '')

        self.svg_file.write(u'{indent}<ellipse cx="{cx!s}" cy="{cy!s}" rx="{rx!s}" ry="{ry!s}" stroke="{outline_color}" stroke-width="{width!s}px" fill="{fill_color}"/>\n'.format(indent = '    ' * self.svg_indent_level, cx = 0.5 * (coords[0] + coords[2]), cy = 0.5 * (coords[1] + coords[3]), rx = 0.5 * (coords[2] - coords[0]), ry = 0.5 * (coords[3] - coords[1]), outline_color = outline_color, width = line_weight, fill_color = fill_color))

    def svg_draw_line(self, **kwargs):
        coords = kwargs.get('coords', [])
        fill = kwargs.get('fill', '')
        line_style = kwargs.get('dash', ())
        line_weight = kwargs.get('width', 1.)
        name = kwargs.get('name', '')

        if len(coords) >= 4:
            self.svg_file.write(u'{indent}<polyline points="{x1!s}'.format(indent = '    ' * self.svg_indent_level, x1 = coords[0]))
            for i in range(1, len(coords)):
                if (i % 2) == 1:
                    self.svg_file.write(u',{y!s}'.format(y = coords[i]))
                else:
                    self.svg_file.write(u' {x!s}'.format(x = coords[i]))
            if len(line_style) == 0:
                self.svg_file.write(u'" stroke="{color}" stroke-width="{width!s}px" fill="none"/>\n'.format(color = fill, width = line_weight))
            else:
                self.svg_file.write(u'" stroke="{color}" stroke-width="{width!s}px" fill="none" stroke-dasharray="{dash}"/>\n'.format(color = fill, width = line_weight, dash = ', '.join([str(n) for n in line_style])))

    def svg_draw_text(self, **kwargs):
        text = kwargs.get('text', '')
        coords = kwargs.get('coords', [])
        fill = kwargs.get('fill', '')
        font = kwargs.get('font', (self.label_font, self.label_fontsize))
        anchor = kwargs.get('anchor', 'center')
        justify = kwargs.get('justify', 'center')
        name = kwargs.get('name', '')

        if anchor == 'center':
            coords[1] += 0.25 * font[1]
            text_anchor = 'middle'
        elif anchor == 'n':
            coords[1] += 0.75 * font[1]
            text_anchor = 'middle'
        elif anchor == 'ne':
            coords[1] += 0.75 * font[1]
            text_anchor = 'end'
        elif anchor == 'e':
            coords[1] += 0.25 * font[1]
            text_anchor = 'end'
        elif anchor == 'se':
            coords[1] -= 0.25 * font[1]
            text_anchor = 'end'
        elif anchor == 's':
            coords[1] -= 0.25 * font[1]
            text_anchor = 'middle'
        elif anchor == 'sw':
            coords[1] -= 0.25 * font[1]
            text_anchor = 'start'
        elif anchor == 'w':
            coords[1] += 0.25 * font[1]
            text_anchor = 'start'
        elif anchor == 'nw':
            coords[1] += 0.75 * font[1]
            text_anchor = 'start'
        else:
            raise ValueError('anchor value must be "center", "n", "ne", "e", "se", "s", "sw", "w", or "nw".')

        self.svg_file.write(u'{indent}<text x="{x!s}" y="{y!s}" fill="{fill}" text-anchor="{text_anchor}" font-family="{font_name}" font-size="{font_size!s}">{text}</text>\n'.format(indent = '    ' * self.svg_indent_level, x = coords[0], y = coords[1], fill = fill, text_anchor = text_anchor, font_name = font[0], font_size = font[1], text = text))

    def svg_begin_group(self, **kwargs):
        name = kwargs.get('name', '')

        if name != '':
            self.svg_file.write(u'{indent}<g id="{name}">\n'.format(indent = '    ' * self.svg_indent_level, name = name))
        else:
            self.svg_file.write(u'{indent}<g>\n'.format(indent = '    ' * self.svg_indent_level))
        self.svg_indent_level += 1

    def svg_end_group(self, **kwargs):
        self.svg_indent_level -= 1
        if self.svg_indent_level < 0:
            self.svg_intent_level = 0
        self.svg_file.write(u'{indent}</g>\n'.format(indent = '    ' * self.svg_indent_level))

