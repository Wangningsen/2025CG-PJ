import cadquery as cq
w0=cq.Workplane('YZ',origin=(-1,0,0))
w1=cq.Workplane('XY',origin=(0,0,-20))
r=w0.sketch().segment((-58,-30),(27,-30)).segment((27,-1)).segment((-5,24)).segment((0,30)).segment((-58,30)).close().assemble().finalize().extrude(101).union(w1.sketch().segment((-100,16),(-58,16)).segment((-58,46)).arc((-81,46),(-100,58)).close().assemble().finalize().extrude(35))