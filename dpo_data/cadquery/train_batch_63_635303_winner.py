import cadquery as cq
w0=cq.Workplane('YZ',origin=(70,0,0))
r=w0.sketch().segment((-100,-19),(-94,-36)).segment((-1,-1)).segment((-1,-50)).arc((26,-58),(54,-53)).segment((90,-57)).segment((100,44)).segment((64,47)).arc((35,58),(4,53)).segment((-30,57)).segment((-31,43)).segment((-1,43)).segment((-1,19)).close().assemble().finalize().extrude(-140)