import cadquery as cq
w0=cq.Workplane('YZ',origin=(7,0,0))
w1=cq.Workplane('YZ',origin=(37,0,0))
r=w0.sketch().segment((-41,-28),(-16,-28)).arc((3,-34),(21,-28)).segment((47,-28)).segment((47,16)).segment((21,16)).arc((3,22),(-16,16)).segment((-41,16)).close().assemble().finalize().extrude(-107).union(w0.sketch().circle(68).push([(49,22)]).circle(9,mode='s').finalize().extrude(78)).union(w1.sketch().segment((-32,5),(32,5)).arc((0,22),(-32,5)).assemble().finalize().extrude(63))