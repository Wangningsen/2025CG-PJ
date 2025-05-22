import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-75,-38),(-2,-38)).segment((-2,-41)).segment((75,-41)).segment((75,41)).segment((-2,41)).segment((-2,18)).segment((-75,18)).close().assemble().finalize().extrude(-200)