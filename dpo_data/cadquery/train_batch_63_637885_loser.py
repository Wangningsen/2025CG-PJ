import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,15))
w1=cq.Workplane('YZ',origin=(-1,0,0))
r=w0.sketch().segment((-100,16),(-58,16)).segment((-58,45)).arc((-83,46),(-100,58)).close().assemble().finalize().extrude(-35).union(w1.sketch().segment((-58,-30),(27,-30)).segment((27,-1)).segment((25,-1)).arc((12,11),(-4,21)).segment((-4,30)).segment((-58,30)).close().assemble().finalize().extrude(101))