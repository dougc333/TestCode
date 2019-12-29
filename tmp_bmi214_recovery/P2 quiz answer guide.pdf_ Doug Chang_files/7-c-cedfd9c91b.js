(window["canvasWebpackJsonp"]=window["canvasWebpackJsonp"]||[]).push([[7],{"3Zzb":function(e,t,n){"use strict"
var o=n("1OyB")
var i=n("vuIU")
var r=n("md7G")
var a=n("foSv")
var s=n("Ji7U")
var u=n("q1tI")
var c=n.n(u)
var l=n("17x9")
var f=n.n(l)
var h=n("i8i4")
var d=n.n(h)
var p=n("AdN2")
var v=n("VTBJ")
var m=n("Ff2n")
var b=n("jtGx")
var y=n("FOOe")
var O,_,g,E
var k=(O=Object(y["a"])(),O(_=(E=g=function(e){Object(s["a"])(t,e)
function t(e){var n
Object(o["a"])(this,t)
n=Object(r["a"])(this,Object(a["a"])(t).call(this,e))
n.state={mountNode:n.findMountNode(e)}
return n}Object(i["a"])(t,[{key:"componentDidMount",value:function(){this.props.open&&"function"===typeof this.props.onOpen&&this.props.onOpen(this.DOMNode)}},{key:"componentDidUpdate",value:function(e){var t=this.findMountNode(this.props)
t!==this.state.mountNode&&this.setState({mountNode:t})
this.props.open&&!e.open&&"function"===typeof this.props.onOpen&&this.props.onOpen(this.DOMNode)
!this.props.open&&e.open&&"function"===typeof this.props.onClose&&this.props.onClose()}},{key:"componentWillUnmount",value:function(){this.removeNode()
this.props.open&&"function"===typeof this.props.onClose&&this.props.onClose()}},{key:"render",value:function(){var e=this.props.children
return this.props.open&&c.a.Children.count(e)>0?d.a.createPortal(e,this.insertNode()):null}},{key:"removeNode",value:function(){if(this.DOMNode&&this.DOMNode.parentNode&&"function"===typeof this.DOMNode.parentNode.removeChild){this.DOMNode.parentNode.removeChild(this.DOMNode)
this.DOMNode=null
this.props.elementRef(this.DOMNode)}}},{key:"insertNode",value:function(){var e=this.props,t=(e.open,e.insertAt),n=(e.onOpen,e.onClose,e.mountNode,e.children,e.elementRef),o=Object(m["a"])(e,["open","insertAt","onOpen","onClose","mountNode","children","elementRef"])
if(!this.DOMNode){var i=document.createElement("span")
var r=Object(v["a"])({},Object(b["b"])(o),{dir:this.dir})
Object.keys(r).forEach((function(e){i.setAttribute(e,r[e])}))
n(i)
this.DOMNode=i}this.DOMNode.parentNode!==this.state.mountNode&&("bottom"===t?this.state.mountNode.appendChild(this.DOMNode):this.state.mountNode.insertBefore(this.DOMNode,this.state.mountNode.firstChild))
return this.DOMNode}},{key:"findMountNode",value:function(e){var t
"function"===typeof e.mountNode?t=e.mountNode():e.mountNode&&(t=e.mountNode)
t&&t.nodeName||(t=document.body)
return t}},{key:"node",get:function(){return this.DOMNode}}])
t.displayName="ReactPortal"
return t}(c.a.Component),g.propTypes={open:f.a.bool,onOpen:f.a.func,onClose:f.a.func,mountNode:f.a.oneOfType([p["a"],f.a.func]),insertAt:f.a.oneOf(["bottom","top"]),children:f.a.node,elementRef:f.a.func},g.defaultProps={open:false,insertAt:"bottom",onOpen:function(e){},onClose:function(){},mountNode:void 0,children:null,elementRef:function(e){}},E))||_)
var N=n("0mOT")
var j,C,D,F
var R=(j=Object(y["a"])(),j(C=(F=D=function(e){Object(s["a"])(t,e)
function t(){Object(o["a"])(this,t)
return Object(r["a"])(this,Object(a["a"])(t).apply(this,arguments))}Object(i["a"])(t,[{key:"componentDidMount",value:function(){this.renderPortal(this.props)}},{key:"shouldComponentUpdate",value:function(e,t){return!(Object(N["a"])(this.props,e)&&Object(N["a"])(this.state,t))}},{key:"componentWillReceiveProps",value:function(e){this.renderPortal(e)}},{key:"componentWillUnmount",value:function(){this.removePortal(this.props)}},{key:"render",value:function(){return null}},{key:"renderPortal",value:function(e){var t=this
var n=e.open,o=e.insertAt,i=e.onOpen,r=(e.onClose,e.elementRef),a=e.children,s=Object(m["a"])(e,["open","insertAt","onOpen","onClose","elementRef","children"])
var u=!this.DOMNode
var l=this.mountNode
var f=a
"string"===typeof f&&f.length>0&&(f=c.a.createElement("span",null,f))
if(n&&c.a.Children.count(f)>0){if(!this.DOMNode){var h=document.createElement("span")
var p=Object(v["a"])({},Object(b["b"])(s),{dir:this.dir})
Object.keys(p).forEach((function(e){h.setAttribute(e,p[e])}))
r(h)
this.DOMNode=h}this.DOMNode.parentNode!==l&&("bottom"===o?l.appendChild(this.DOMNode):l.insertBefore(this.DOMNode,l.firstChild))
var y=function(){(u||!t.props.open&&n)&&"function"===typeof i&&i(t.DOMNode)}
d.a.unstable_renderSubtreeIntoContainer(this,f,this.DOMNode,y)}else this.removePortal(e)}},{key:"removePortal",value:function(e){var t
if(this.DOMNode){t=d.a.unmountComponentAtNode(this.DOMNode)
this.DOMNode.parentNode&&this.DOMNode.parentNode.removeChild(this.DOMNode)
this.DOMNode=null
this.props.elementRef(this.DOMNode)}t&&"function"===typeof e.onClose&&e.onClose()}},{key:"mountNode",get:function(){var e
"function"===typeof this.props.mountNode?e=this.props.mountNode():this.props.mountNode&&(e=this.props.mountNode)
e&&e.nodeName||(e=document.body)
return e}},{key:"DOMNode",get:function(){return this._node},set:function(e){this._node=e}},{key:"node",get:function(){return this.DOMNode}}])
t.displayName="SubtreePortal"
return t}(u["Component"]),D.propTypes={open:f.a.bool,onOpen:f.a.func,onClose:f.a.func,mountNode:f.a.oneOfType([p["a"],f.a.func]),insertAt:f.a.oneOf(["bottom","top"]),children:f.a.node,elementRef:f.a.func},D.defaultProps={open:false,insertAt:"bottom",onOpen:function(e){},onClose:function(){},mountNode:null,children:null,elementRef:function(e){}},F))||C)
n.d(t,"a",(function(){return M}))
var w="function"===typeof d.a.createPortal
var M=function(e){Object(s["a"])(t,e)
function t(){var e
var n
Object(o["a"])(this,t)
for(var i=arguments.length,s=new Array(i),u=0;u<i;u++)s[u]=arguments[u]
n=Object(r["a"])(this,(e=Object(a["a"])(t)).call.apply(e,[this].concat(s)))
n.handleElementRef=function(e){if(e){n.DOMNode=e
"function"===typeof n.props.elementRef&&n.props.elementRef(e)}}
return n}Object(i["a"])(t,[{key:"render",value:function(){return w?c.a.createElement(k,Object.assign({},this.props,{elementRef:this.handleElementRef})):c.a.createElement(R,Object.assign({},this.props,{elementRef:this.handleElementRef}))}}])
t.displayName="Portal"
return t}(u["Component"])
M.propTypes={open:f.a.bool,onOpen:f.a.func,onClose:f.a.func,mountNode:f.a.oneOfType([p["a"],f.a.func]),insertAt:f.a.oneOf(["bottom","top"]),children:f.a.node,elementRef:f.a.func}
M.defaultProps={open:false,insertAt:"bottom",onOpen:function(e){},onClose:function(){},mountNode:null,children:null,elementRef:function(e){}}},AdN2:function(e,t,n){"use strict"
n.d(t,"a",(function(){return a}))
var o=n("17x9")
var i=n.n(o)
var r=!!("undefined"!==typeof window&&window.document&&window.document.createElement)
var a=r?i.a.oneOfType([i.a.element,i.a.instanceOf(Element)]):i.a.element},CyAq:function(e,t,n){"use strict"
n.d(t,"a",(function(){return o}))
function o(e){var t="".concat(e)
return[parseFloat(t,10),t.match(/[\d.\-\+]*\s*(.*)/)[1]||""]}},EgqM:function(e,t,n){"use strict"
n.d(t,"a",(function(){return s}))
var o=n("QF4Q")
var i=n("i/8D")
function r(e,t){var n=Object(o["a"])(e)
var i=Object(o["a"])(t)
return!(!n||!i)&&(n.contains?n.contains(i):n.compareDocumentPosition?n===i||!!(16&n.compareDocumentPosition(i)):a(n,i))}function a(e,t){var n=t
while(n){if(n===e)return true
n=n.parentNode}return false}var s=i["a"]?r:a},ISHz:function(e,t,n){"use strict"
n.d(t,"a",(function(){return i}))
var o=n("i/8D")
var i=function(){var e
if(o["a"]&&window.requestAnimationFrame&&window.cancelAnimationFrame)e=function(e){var t=window.requestAnimationFrame(e)
return{cancel:function(){return window.cancelAnimationFrame(t)}}}
else{var t=(new Date).getTime()
e=function(e){var n=(new Date).getTime()
var o=Math.max(0,16-(n-t))
var i=setTimeout(e,o)
t=n
return{cancel:function(){return clearTimeout(i)}}}}return e}()},"K7t/":function(e,t,n){"use strict"
n.d(t,"a",(function(){return a}))
var o=n("QF4Q")
var i=n("EgqM")
var r=n("pgSO")
function a(e){var t=e&&Object(o["a"])(e)
var n=Object(r["a"])()
return t&&(n===t||Object(i["a"])(t,n))}},cFoZ:function(e,t,n){"use strict"
var o=n("KQm4")
var i=n("QF4Q")
function r(e,t){var n=e&&Object(i["a"])(e)
if(!n)return false
return n.matches?n.matches(t):n.msMatchesSelector(t)}var a=n("IPIv")
n.d(t,"a",(function(){return s}))
function s(e,t,n){var a=Object(i["a"])(e)
if(!a||"function"!==typeof a.querySelectorAll)return[]
var s="a[href],frame,iframe,object,input:not([type=hidden]),select,textarea,button,*[tabindex]"
var u=Array.from(a.querySelectorAll(s))
n&&r(a,s)&&(u=[].concat(Object(o["a"])(u),[a]))
return u.filter((function(e){return"function"===typeof t?t(e)&&f(e):f(e)}))}function u(e){var t=Object(a["a"])(e)
return"inline"!==t.display&&e.offsetWidth<=0&&e.offsetHeight<=0||"none"===t.display}function c(e){var t=["fixed","absolute"]
if(t.includes(e.style.position.toLowerCase()))return true
if(t.includes(Object(a["a"])(e).getPropertyValue("position").toLowerCase()))return true
return false}function l(e){while(e){if(e===document.body)break
if(u(e))return false
if(c(e))break
e=e.parentNode}return true}function f(e){return!e.disabled&&l(e)}},"e+xl":function(e,t,n){"use strict"
n.d(t,"a",(function(){return i}))
var o=n("cFoZ")
function i(e,t){return Object(o["a"])(e,(function(e){return!r(e.getAttribute("tabindex"))}),t)}function r(e){return!isNaN(e)&&e<0}},hGMy:function(e,t,n){"use strict"
n.d(t,"a",(function(){return u}))
var o=n("QF4Q")
var i=n("K7t/")
var r=n("pgSO")
var a=n("/UXv")
var s=n("e+xl")
function u(e,t,n){var u=Object(o["a"])(e)
var c=Object(s["a"])(u)
if(!c.length){t.preventDefault()
return}if(Object(i["a"])(e)){var l=Object(r["a"])();-1===c.indexOf(l)&&c.push(l)}var f=c[t.shiftKey?0:c.length-1]
var h=Object(a["a"])(f)||Object(a["a"])(u)||!Object(i["a"])(e)
if(!h)return
if("function"===typeof n){n()
return}t.preventDefault()
var d=c[t.shiftKey?c.length-1:0]
d.focus()}},"o/UQ":function(e,t,n){"use strict"
var o=n("VTBJ")
var i=n("Ff2n")
var r=n("1OyB")
var a=n("vuIU")
var s=n("md7G")
var u=n("foSv")
var c=n("Ji7U")
n("DEX3")
var l=n("q1tI")
var f=n.n(l)
var h=n("17x9")
var d=n.n(h)
var p=n("KgFQ")
var v=n("jtGx")
var m=n("ISHz")
var b=n("QF4Q")
var y=n("3zPy")
var O=n.n(y)
var _=n("EgqM")
var g=n("DUTp")
var E=n("yfCu")
function k(e){try{return e.contentDocument||e.contentWindow.document}catch(e){return null}}var N=n("BTe1")
var j=n("e+xl")
var C=function(){function e(t){var n=this
var o=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{shouldContainFocus:true,liveRegion:[]}
Object(r["a"])(this,e)
this._observer=null
this._attributes=[]
this._nodes=[]
this._parents=[]
this.handleDOMMutation=function(e){e.forEach((function(e){var t=Array.from(e.addedNodes)
var o=Array.from(e.removedNodes)
n.hideNodes(t)
o.forEach((function(e){"iframe"!==e.tagName.toLowerCase()&&n.restoreNode(e)
var t=n.parseIframeBodies(e)
t.forEach((function(e){n.restoreNode(e)}))}))}))}
var i="function"===typeof o.liveRegion?o.liveRegion():o.liveRegion
this._liveRegion=Array.isArray(i)?i:[i]
this._contextElement=t
this._options=o}Object(a["a"])(e,[{key:"updateElement",value:function(e){this._contextElement=e}},{key:"muteNode",value:function(e){var t=this
if(e&&"script"!==e.tagName.toLowerCase()){["role","aria-label","aria-hidden"].forEach((function(n){var o=e.getAttribute(n)
if(null!==o){t._attributes.push([e,n,o])
e.removeAttribute(n)}}))
this._observer.observe(e,{childList:true})}}},{key:"hideNodes",value:function(e){var t=this
e.forEach((function(e){if(e&&1===e.nodeType&&"script"!==e.tagName.toLowerCase()&&-1===t._parents.indexOf(e)&&-1===t._nodes.indexOf(e)&&-1===t._liveRegion.indexOf(e)&&!t._contextElement.contains(e)){"iframe"!==e.tagName.toLowerCase()&&t.hideNode(e)
var n=t.parseIframeBodies(e)
n.forEach((function(e){t.hideNode(e)}))}}))}},{key:"hideNode",value:function(e){if("true"!==e.getAttribute("aria-hidden")){e.setAttribute("aria-hidden","true")
this._nodes.push(e)}}},{key:"restoreNode",value:function(e){var t=this._nodes.indexOf(e)
if(t>=0){e.removeAttribute("aria-hidden")
this._nodes.splice(t,1)}}},{key:"parseIframeBodies",value:function(e){if(!e)return[]
var t=[]
"iframe"===e.tagName.toLowerCase()?t.push(e):e.getElementsByTagName&&(t=Array.from(e.getElementsByTagName("iframe")))
return t.map((function(e){var t=null
try{t=e.contentDocument.body}catch(e){"[ui-a11y] could not find a document for iframe: ".concat(e)}return t})).filter((function(e){return null!==e}))}},{key:"activate",value:function(){if(!this._options.shouldContainFocus)return
this._observer=new MutationObserver(this.handleDOMMutation)
var e=this._contextElement
while(e&&1===e.nodeType&&"body"!==e.tagName.toLowerCase()){var t=e.parentElement
if(t){this._parents.push(t)
this.muteNode(t)
this.hideNodes(Array.prototype.slice.call(t.childNodes))}e=e.parentNode}}},{key:"deactivate",value:function(){if(this._observer){this._observer.disconnect()
this._observer=null}this._nodes.forEach((function(e){e.removeAttribute("aria-hidden")}))
this._nodes=[]
this._attributes.forEach((function(e){e[0].setAttribute(e[1],e[2]||"")}))
this._attributes=[]
this._parents=[]}}])
return e}()
var D=n("K7t/")
var F=n("gpCx")
var R=n("pgSO")
var w=n("hGMy")
var M=n("cFoZ")
var x=function(){function e(t,n){var o=this
Object(r["a"])(this,e)
this._contextElement=null
this._focusLaterElement=null
this._needToFocus=false
this._listeners=[]
this._raf=[]
this._active=false
this.handleDismiss=function(e){o._options.onDismiss(e)}
this.handleKeyDown=function(e){e.keyCode===O.a.codes.tab&&Object(w["a"])(o._contextElement,e)}
this.handleClick=function(e){o._wasDocumentClick=true}
this.handleWindowBlur=function(e){if(o._wasDocumentClick){o._wasDocumentClick=false
return}o._needToFocus=true}
this.handleFocus=function(e){if(o._needToFocus){o._needToFocus=false
if(!o._contextElement)return
o._raf.push(Object(m["a"])((function(){if(Object(D["a"])(o._contextElement))return
o.focusDefaultElement()})))}}
this.handleFirstTabbableKeyDown=function(e){e.keyCode===O.a.codes.tab&&e.shiftKey&&o._options.onBlur(e)}
this.handleLastTabbableKeyDown=function(e){e.keyCode!==O.a.codes.tab||e.shiftKey||o._options.onBlur(e)}
this._contextElement=Object(b["a"])(t)
this._options=n||{shouldContainFocus:true,shouldReturnFocus:true,onBlur:function(e){},onDismiss:function(e){},defaultFocusElement:null}
this._options.shouldReturnFocus&&(this._focusLaterElement=this.activeElement)}Object(a["a"])(e,[{key:"updateElement",value:function(e){this._contextElement=Object(b["a"])(e)}},{key:"focusDefaultElement",value:function(){var e=this.defaultFocusElement,t=this.shouldContainFocus
e?e.focus():t&&this.activeElement.blur()}},{key:"focus",value:function(){var e=this
if(this.focused)return
this._raf.push(Object(m["a"])((function(){e.focusDefaultElement()})))}},{key:"blur",value:function(){if(this._options.shouldReturnFocus&&this._focusLaterElement){try{this._focusLaterElement.focus()}catch(e){"\n          [KeyboardFocusRegion] You tried to return focus to ".concat(this._focusLaterElement,"\n          but it is not in the DOM anymore: ").concat(e,"\n          ")}this._focusLaterElement=null}}},{key:"activate",value:function(){var e=this.defaultFocusElement,t=this.shouldContainFocus
if(!this._active&&(e||t)){if(t)this._listeners.push(Object(E["a"])(this.doc,"keydown",this.handleKeyDown))
else{this._listeners.push(Object(E["a"])(this.firstTabbable||e,"keydown",this.handleFirstTabbableKeyDown))
this._listeners.push(Object(E["a"])(this.lastTabbable||e,"keydown",this.handleLastTabbableKeyDown))}this._listeners.push(Object(E["a"])(this.doc,"click",this.handleClick,true))
this._listeners.push(Object(E["a"])(this.win,"blur",this.handleWindowBlur,false))
this._listeners.push(Object(E["a"])(this.doc,"focus",this.handleFocus,true))
this._active=true}}},{key:"deactivate",value:function(){if(this._active){this._listeners.forEach((function(e){e.remove()}))
this._listeners=[]
this._raf.forEach((function(e){return e.cancel()}))
this._raf=[]
this._preventCloseOnDocumentClick=false
this._active=false}}},{key:"focused",get:function(){return Object(D["a"])(this._contextElement)}},{key:"shouldContainFocus",get:function(){var e=this._options.shouldContainFocus
return true===e||Array.isArray(e)&&e.includes["keyboard"]}},{key:"focusable",get:function(){return Object(M["a"])(this._contextElement,(function(){return true}),true)||[]}},{key:"tabbable",get:function(){return Object(j["a"])(this._contextElement)||[]}},{key:"firstTabbable",get:function(){return this.tabbable[0]}},{key:"lastTabbable",get:function(){return this.tabbable.pop()}},{key:"firstFocusable",get:function(){return this.focusable[0]}},{key:"lastFocusable",get:function(){return this.focusable.pop()}},{key:"doc",get:function(){return Object(g["a"])(this._contextElement)}},{key:"win",get:function(){return Object(F["a"])(this._contextElement)}},{key:"activeElement",get:function(){return Object(R["a"])(this.doc)}},{key:"defaultFocusElement",get:function(){var e=this._options.defaultFocusElement
var t=Object(b["a"])("function"===typeof e?e():e)
if(t&&this._contextElement&&this._contextElement.contains(t))return t
var n=this.firstTabbable
if(n)return n
if(this.focusable.includes(this._contextElement))return this._contextElement
return null}}])
return e}()
var A=function(){function e(t,n){var o=this
Object(r["a"])(this,e)
this._contextElement=null
this._preventCloseOnDocumentClick=false
this._listeners=[]
this._active=false
this.handleDismiss=function(e,t){o._options.onDismiss(e,t)}
this.captureDocumentClick=function(e){var t=e.target
o._preventCloseOnDocumentClick=0!==e.button||Object(_["a"])(o._contextElement,t)}
this.handleDocumentClick=function(e){o._options.shouldCloseOnDocumentClick&&!o._preventCloseOnDocumentClick&&o.handleDismiss(e,true)}
this.handleFrameClick=function(e,t){Object(_["a"])(o._contextElement,t)||o.handleDismiss(e,true)}
this.handleKeyUp=function(e){o._options.shouldCloseOnEscape&&e.keyCode===O.a.codes.escape&&!e.defaultPrevented&&o.handleDismiss(e)}
this._options=n||{shouldCloseOnDocumentClick:true,shouldCloseOnEscape:true,onDismiss:function(e){}}
this._contextElement=t
this._screenReaderFocusRegion=new C(t,n)
this._keyboardFocusRegion=new x(t,n)
this._id=Object(N["a"])()}Object(a["a"])(e,[{key:"updateElement",value:function(e){this._contextElement=e
this._keyboardFocusRegion&&this._keyboardFocusRegion.updateElement(e)
this._screenReaderFocusRegion&&this._screenReaderFocusRegion.updateElement(e)}},{key:"activate",value:function(){var e=this
if(!this._active){var t=Object(g["a"])(this._contextElement)
this._keyboardFocusRegion.activate()
this._screenReaderFocusRegion.activate()
if(this._options.shouldCloseOnDocumentClick){this._listeners.push(Object(E["a"])(t,"click",this.captureDocumentClick,true))
this._listeners.push(Object(E["a"])(t,"click",this.handleDocumentClick))
Array.from(t.getElementsByTagName("iframe")).forEach((function(t){var n=k(t)
n&&e._listeners.push(Object(E["a"])(n,"mouseup",(function(n){e.handleFrameClick(n,t)})))}))}this._options.shouldCloseOnEscape&&this._listeners.push(Object(E["a"])(t,"keyup",this.handleKeyUp))
this._active=true}}},{key:"deactivate",value:function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{},t=e.keyboard,n=void 0===t||t
if(this._active){this._listeners.forEach((function(e){e.remove()}))
this._listeners=[]
n&&this._keyboardFocusRegion.deactivate()
this._screenReaderFocusRegion.deactivate()
this._active=false}}},{key:"focus",value:function(){this._active
this._keyboardFocusRegion.focus()}},{key:"blur",value:function(){this._active
this._keyboardFocusRegion.blur()}},{key:"id",get:function(){return this._id}},{key:"focused",get:function(){return this._active}},{key:"keyboardFocusable",get:function(){return(Object(j["a"])(this._contextElement)||[]).length>0}}])
return e}()
var T=[]
var P=function e(){Object(r["a"])(this,e)}
P.focusRegion=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{}
var n
n="string"===typeof t?P.getEntry(e,t):P.addEntry(e,t)
if(n&&n.region&&"function"===typeof n.region.focus){n.region.focus()
return n.region}"[FocusRegionManager] Could not focus region with element: ".concat(e)}
P.activateRegion=function(e,t){var n=P.addEntry(e,t),o=n.region
return o}
P.getActiveEntry=function(){return T.find((function(e){var t=e.region
return t.focused}))}
P.findEntry=function(e,t){var n
n=t?T.findIndex((function(e){return e.id===t})):T.findIndex((function(t){return t.element===e}))
return n}
P.getEntry=function(e,t){return T[P.findEntry(e,t)]}
P.addEntry=function(e){var t=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{}
var n=new A(e,t)
var o=P.getActiveEntry()
var i=n.keyboardFocusable
T.forEach((function(e){var t=e.region
t&&t.deactivate(t.focused&&!i&&{keyboard:false})}))
n.activate()
t.shouldFocusOnOpen&&n.focus()
var r={id:n.id,element:e,region:n,children:[],parent:o}
T.push(r)
o&&o.children.push(r)
return r}
P.removeEntry=function(e,t){var n=P.findEntry(e,t)
var o=T[n]
n>-1&&T.splice(n,1)
return o}
P.isFocused=function(e,t){var n=P.getActiveEntry()
return t?n&&n.region&&n.id===t:n&&n.region&&n.element===e}
P.clearEntries=function(){T=[]}
P.blurRegion=function(e,t){var n=P.removeEntry(e,t)
if(n){var o=n.children,i=n.region,r=n.parent
i&&i.deactivate()
o&&o.forEach((function(e){var t=e.id,n=e.element
var o=P.removeEntry(n,t)
o&&o.region&&o.region.deactivate()}))
r&&r.region&&r.region.activate()
i&&i.blur()}}
n.d(t,"a",(function(){return B}))
var B=function(e){Object(c["a"])(t,e)
function t(){var e
var n
Object(r["a"])(this,t)
for(var o=arguments.length,i=new Array(o),a=0;a<o;a++)i[a]=arguments[a]
n=Object(s["a"])(this,(e=Object(u["a"])(t)).call.apply(e,[this].concat(i)))
n._raf=[]
n._focusRegion=null
n.getRef=function(e){n._root=e}
return n}Object(a["a"])(t,[{key:"componentDidMount",value:function(){this.props.open&&this.open()}},{key:"componentDidUpdate",value:function(e){var t=this.props.open
t&&!e.open?this.open():!t&&e.open&&this.close()
this._focusRegion&&this._focusRegion.updateElement(this.contentElement)}},{key:"componentWillUnmount",value:function(){this.props.open&&this.close()
this._raf.forEach((function(e){return e.cancel()}))
this._raf=[]}},{key:"open",value:function(){var e=this
var t=this.props,n=(t.open,t.contentElement,Object(i["a"])(t,["open","contentElement"]))
this._raf.push(Object(m["a"])((function(){e._focusRegion=P.activateRegion(e.contentElement,Object(o["a"])({},n))})))}},{key:"close",value:function(){this._focusRegion&&P.blurRegion(this.contentElement,this._focusRegion.id)}},{key:"focus",value:function(){if(!this.props.open||!this.contentElement)return
this._focusRegion&&P.focusRegion(this.contentElement,this._focusRegion.id)}},{key:"blur",value:function(){if(!this.props.open||!this.contentElement)return
this.close()}},{key:"render",value:function(){var e=Object(p["a"])(t,this.props)
return this.props.open?f.a.createElement(e,Object.assign({},Object(v["a"])(this.props,t.propTypes),{ref:this.getRef,role:this.props.label?"dialog":null,"aria-label":this.props.label,className:this.props.className}),this.props.children):null}},{key:"contentElement",get:function(){var e=Object(b["a"])(this.props.contentElement)
e||(e=Object(b["a"])(this._root))
return e}},{key:"focused",get:function(){return this.contentElement&&this._focusRegion&&P.isFocused(this.contentElement,this._focusRegion.id)}}])
t.displayName="Dialog"
return t}(l["Component"])
B.propTypes={children:d.a.node,as:d.a.elementType,display:d.a.oneOf(["auto","block","inline-block"]),label:d.a.string,open:d.a.bool,onBlur:d.a.func,onDismiss:d.a.func,defaultFocusElement:d.a.oneOfType([d.a.element,d.a.func]),contentElement:d.a.oneOfType([d.a.element,d.a.func]),liveRegion:d.a.oneOfType([d.a.arrayOf(d.a.element),d.a.element,d.a.func]),shouldContainFocus:d.a.oneOfType([d.a.bool,d.a.oneOf(["keyboard","screenreader"])]),shouldReturnFocus:d.a.bool,shouldCloseOnDocumentClick:d.a.bool,shouldCloseOnEscape:d.a.bool,shouldFocusOnOpen:d.a.bool}
B.defaultProps={children:null,display:void 0,label:void 0,open:false,shouldFocusOnOpen:true,shouldContainFocus:false,shouldReturnFocus:false,shouldCloseOnDocumentClick:true,shouldCloseOnEscape:true,defaultFocusElement:null,contentElement:null,liveRegion:null,onBlur:function(e){},onDismiss:function(e){}}},yfCu:function(e,t,n){"use strict"
n.d(t,"a",(function(){return i}))
var o=n("QF4Q")
function i(e,t,n,i){var r=e===window||e===document?e:Object(o["a"])(e)
r.addEventListener(t,n,i)
return{remove:function(){r.removeEventListener(t,n,i)}}}}}])

//# sourceMappingURL=7-c-cedfd9c91b.js.map