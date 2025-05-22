import cadquery as cq
w0=cq.Workplane('YZ',origin=(22,0,0))
r=w0.sketch().segment((14,-42),(75,-42)).segment((75,24)).arc((99,42),(69,42)).segment((14,42)).close().assemble().finalize().extrude(-44).union(w0.sketch().segment((-100,-8),(-78,-53)).segment((28,-1)).segment((6,44)).close().assemble().finalize().extrude(-13))