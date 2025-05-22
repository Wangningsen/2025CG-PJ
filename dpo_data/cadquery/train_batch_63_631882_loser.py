import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,35,0))
r=w0.sketch().push([(-74,46)]).circle(26).circle(23,mode='s').reset().face(w0.sketch().segment((-33,-51),(-31,-54)).segment((11,-30)).segment((72,-72)).segment((85,-59)).segment((42,-14)).segment((100,12)).segment((98,15)).segment((46,-13)).segment((-4,31)).segment((-17,18)).segment((27,-26)).close().assemble()).finalize().extrude(-69)