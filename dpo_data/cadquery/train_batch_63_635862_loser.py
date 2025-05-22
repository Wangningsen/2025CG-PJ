import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
w1=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().segment((16,-82),(96,-88)).segment((99,-57)).segment((19,-51)).close().assemble().finalize().extrude(-115).union(w0.workplane(offset=-71/2).moveTo(2.5,45).box(47,16,71)).union(w0.sketch().push([(-32,-61.5)]).rect(56,77).push([(-32,-61)]).circle(14,mode='s').finalize().extrude(-59)).union(w1.sketch().segment((-16,-53),(2,-53)).arc((27,-62),(52,-53)).segment((71,-53)).segment((71,-20)).arc((57,83),(1,0)).arc((1,-3),(2,-7)).segment((-16,-7)).close().assemble().finalize().extrude(-74))