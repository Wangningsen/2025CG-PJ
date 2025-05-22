import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
w1=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().segment((16,-82),(96,-88)).segment((99,-57)).segment((19,-51)).close().assemble().finalize().extrude(-115).union(w0.workplane(offset=-71/2).moveTo(1.5,45).box(49,16,71)).union(w0.sketch().push([(-32,-61.5)]).rect(56,77).push([(-31,-62)]).circle(14,mode='s').finalize().extrude(-59)).union(w1.sketch().segment((-16,-53),(5,-53)).arc((28,-62),(51,-53)).segment((71,-53)).segment((71,-19)).arc((56,83),(0,-2)).segment((-16,-2)).close().assemble().finalize().extrude(-74))