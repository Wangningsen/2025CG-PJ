import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
r=w0.sketch().arc((-24,-78),(-21,-65),(-24,-52)).close().assemble().finalize().extrude(-114).union(w0.sketch().arc((-13,70),(-16,49),(2,36)).segment((-12,46)).segment((-6,54)).segment((10,42)).segment((10,41)).arc((22,66),(-5,76)).arc((-11,72),(-13,70)).assemble().finalize().extrude(86))