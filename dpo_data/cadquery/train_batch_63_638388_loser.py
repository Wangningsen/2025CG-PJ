import cadquery as cq
w0=cq.Workplane('YZ',origin=(-13,0,0))
r=w0.sketch().arc((-12,22),(-24,-98),(17,16)).arc((-1,-1),(-12,22)).assemble().push([(63,97)]).rect(16,6).finalize().extrude(26)