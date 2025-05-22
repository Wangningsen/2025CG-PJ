import cadquery as cq
w0=cq.Workplane('YZ',origin=(1,0,0))
w1=cq.Workplane('YZ',origin=(-23,0,0))
r=w0.sketch().push([(13.5,34.5)]).rect(3,51).reset().face(w0.sketch().arc((47,4),(55,7),(54,-2)).arc((87,48),(47,4)).assemble()).push([(69,25)]).circle(11,mode='s').finalize().extrude(29).union(w1.sketch().segment((-100,-41),(-91,-41)).segment((-91,-60)).segment((-41,-60)).segment((-41,-41)).segment((-33,-41)).segment((-33,-5)).segment((-41,-5)).segment((-41,14)).segment((-91,14)).segment((-91,-5)).segment((-100,-5)).close().assemble().finalize().extrude(-7))