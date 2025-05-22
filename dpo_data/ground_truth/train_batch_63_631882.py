import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,34,0))
r=w0.sketch().push([(-74,46)]).circle(26).circle(23,mode='s').reset().face(w0.sketch().segment((-32,-50),(-31,-54)).segment((27,-25)).segment((72,-72)).segment((85,-59)).segment((44,-16)).segment((100,12)).segment((98,15)).segment((42,-14)).segment((-4,31)).segment((-17,18)).segment((24,-22)).close().assemble()).finalize().extrude(-69)