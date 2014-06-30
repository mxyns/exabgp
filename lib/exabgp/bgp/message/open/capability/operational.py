# encoding: utf-8
"""
operational.py

Created by Thomas Mangin on 2013-09-01.
Copyright (c) 2013-2013 Exa Networks. All rights reserved.
"""

from exabgp.bgp.message.open.capability import Capability
from exabgp.bgp.message.open.capability.id import CapabilityID


# =================================================================== Operational
#

class Operational (Capability,list):
	ID = CapabilityID.OPERATIONAL

	def __str__ (self):
		# XXX: FIXME: could be more verbose
		return 'Operational'

	def extract (self):
		return ['']

	@staticmethod
	def unpack (capability,instance,data):
		# XXX: FIXME: we should set that that instance was seen and raise if seen twice
		return instance
