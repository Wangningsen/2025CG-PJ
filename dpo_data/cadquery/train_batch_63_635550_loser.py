import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-72,-22),(-21,-35)).arc((-11,-39),(-1,-41)).segment((55,-53)).segment((72,19)).segment((47,26)).arc((19,51),(-19,47)).segment((-25,44)).arc((-30,44),(-34,43)).segment((-37,46)).segment((-39,44)).segment((-55,51)).close().assemble().finalize().extrude(200)