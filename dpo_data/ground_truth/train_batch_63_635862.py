import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,31))
w1=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().segment((16,-82),(96,-88)).segment((99,-57)).segment((19,-51)).close().assemble().finalize().extrude(-115).union(w0.workplane(offset=-71/2).moveTo(2.5,45).box(47,16,71)).union(w0.sketch().push([(-32,-61.5)]).rect(56,77).push([(-32,-61)]).circle(14,mode='s').finalize().extrude(-59)).union(w1.sketch().segment((-16,-53),(4,-53)).arc((27,-62),(51,-53)).segment((71,-53)).segment((71,-20)).arc((59,82),(-2,-1)).segment((-16,-1)).close().assemble().finalize().extrude(-74))