import cadquery as cq
w0=cq.Workplane('YZ',origin=(63,0,0))
r=w0.sketch().segment((-82,-100),(60,-100)).segment((60,24)).segment((82,30)).segment((63,88)).segment((60,87)).segment((60,100)).segment((-82,100)).close().assemble().finalize().extrude(-126)