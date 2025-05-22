import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-38))
r=w0.sketch().arc((-99,-87),(-90,-90),(-98,-84)).arc((-97,-86),(-99,-87)).assemble().finalize().extrude(18).union(w0.sketch().segment((43,85),(100,53)).arc((83,87),(43,85)).assemble().finalize().extrude(77))