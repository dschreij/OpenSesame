# coding=utf-8

"""
This file is part of OpenSesame.

OpenSesame is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

OpenSesame is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with OpenSesame.  If not, see <http://www.gnu.org/licenses/>.
"""

from libopensesame.py3compat import *
from openexp._canvas._element.element import Element


class NoisePatch(Element):

	def __init__(self, canvas, x=0, y=0, env=u"gaussian", size=96, stdev=12,
		col1=u"white", col2=u"black", bgmode=u"avg"):

		Element.__init__(self, canvas, x=x, y=y, env=u'gaussian', size=96,
			stdev=12, col1=u'white', col2=u'black', bgmode=u'avg')
