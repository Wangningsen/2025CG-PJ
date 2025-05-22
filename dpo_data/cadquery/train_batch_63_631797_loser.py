import cadquery as cq
w0=cq.Workplane('YZ',origin=(22,0,0))
r=w0.sketch().segment((14,-42),(75,-42)).segment((75,23)).arc((99,43),(69,42)).segment((14,42)).close().assemble().finalize().extrude(-44).union(w0.sketch().segment((-100,-9),(-78,-53)).segment((41,9)).segment((19,53)).close().assemble().finalize().extrude(-13))