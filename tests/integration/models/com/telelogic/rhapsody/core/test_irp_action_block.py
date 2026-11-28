"""IRPActionBlock has no child-owned integration API.

It declares no direct members and inherits its API from IRPMessage. The
model-integration scope rules prohibit asserting inherited methods in this
child-interface file; wrapper inheritance and registration are covered by the
mirrored fake-COM unit tests.
"""
