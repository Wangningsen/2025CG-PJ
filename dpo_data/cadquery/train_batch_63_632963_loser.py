import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-64))
r=w0.sketch().segment((-100,-92),(26,-92)).arc((38,-95),(50,-92)).segment((100,-92)).segment((100,92)).segment((-26,92)).arc((-38,95),(-50,92)).segment((-100,92)).close().assemble().finalize().extrude(128)