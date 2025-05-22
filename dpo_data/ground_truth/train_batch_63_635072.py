import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-13,-38),(13,-38)).segment((13,-32)).arc((1,-15),(22,-12)).arc((25,6),(13,24)).segment((13,38)).segment((-13,38)).segment((-13,24)).arc((-25,0),(-13,-21)).close().assemble().finalize().extrude(-200)