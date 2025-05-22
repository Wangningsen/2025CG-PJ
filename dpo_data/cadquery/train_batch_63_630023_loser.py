import cadquery as cq
w0=cq.Workplane('YZ',origin=(-50,0,0))
w1=cq.Workplane('YZ',origin=(-51,0,0))
r=w0.sketch().push([(21,96)]).rect(132,8).push([(21,96.5)]).rect(2,5,mode='s').finalize().extrude(-41).union(w0.sketch().arc((-59,-10),(71,-66),(-45,17)).segment((-45,-10)).close().assemble().finalize().extrude(141)).union(w1.sketch().segment((9,-34),(95,-34)).segment((95,-21)).segment((9,-21)).segment((9,-25)).segment((12,-25)).segment((12,-27)).segment((9,-27)).close().assemble().push([(52,-28)]).circle(6,mode='s').finalize().extrude(-23))