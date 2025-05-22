import cadquery as cq
w0=cq.Workplane('YZ',origin=(62,0,0))
r=w0.sketch().segment((-60,-99),(58,-100)).segment((60,99)).segment((-58,100)).arc((-25,0),(-60,-99)).assemble().finalize().extrude(-124)