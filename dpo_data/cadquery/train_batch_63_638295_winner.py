import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().circle(95).reset().face(w0.sketch().segment((-77,14),(-38,-4)).arc((-13,-36),(27,-31)).segment((66,-48)).segment((77,-14)).segment((38,4)).arc((13,36),(-27,30)).segment((-66,46)).close().assemble(),mode='s').finalize().extrude(-200)