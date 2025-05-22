import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,70))
r=w0.sketch().arc((-54,-78),(29,-86),(35,-4)).arc((38,81),(-47,84)).segment((-1,89)).segment((4,41)).arc((-25,16),(9,-2)).segment((11,-18)).arc((16,-16),(20,-14)).arc((23,-68),(-31,-76)).close().assemble().finalize().extrude(-141)