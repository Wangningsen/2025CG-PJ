import cadquery as cq
w0=cq.Workplane('YZ',origin=(5,0,0))
r=w0.sketch().segment((-100,-39),(-69,-39)).segment((-69,-38)).segment((-67,-38)).segment((-67,-39)).segment((23,-39)).segment((23,-78)).segment((83,-78)).segment((83,-2)).segment((100,37)).segment((83,44)).segment((83,75)).segment((36,75)).segment((36,78)).segment((-100,78)).close().assemble().finalize().extrude(-10)