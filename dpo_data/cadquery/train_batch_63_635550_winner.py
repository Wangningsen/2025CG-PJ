import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-72,-22),(-3,-41)).arc((3,-41),(9,-42)).segment((55,-53)).segment((72,19)).segment((46,26)).arc((16,51),(-24,44)).segment((-55,51)).close().assemble().finalize().extrude(200)