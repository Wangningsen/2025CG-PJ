import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-92))
r=w0.sketch().segment((-100,-17),(-23,-17)).arc((0,-29),(23,-17)).segment((100,-17)).segment((100,17)).segment((23,17)).arc((0,29),(-23,17)).segment((-100,17)).close().assemble().finalize().extrude(184)