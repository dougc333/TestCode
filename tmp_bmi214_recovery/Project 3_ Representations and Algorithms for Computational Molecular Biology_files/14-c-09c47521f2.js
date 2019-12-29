(window["canvasWebpackJsonp"]=window["canvasWebpackJsonp"]||[]).push([[14],{"5Shj":function(e,t,n){"use strict"
var o=n("Ff2n")
var r=n("1OyB")
var a=n("vuIU")
var i=n("md7G")
var s=n("foSv")
var u=n("Ji7U")
var c=n("q1tI")
var f=n.n(c)
var l=n("17x9")
var d=n.n(l)
var p=n("u9uf")
var h=n("BTe1")
var v=n("J2CL")
var b=n("oXx0")
var m=n("VTBJ")
var y=n("PJ1B")
var O=n("vwVh")
var g=n("KgFQ")
var j=n("jtGx")
var L=n("sQ3t")
var k=n("E+IV")
var w=n("jsCG")
var S=function(e){var t=e.typography,n=e.spacing
return{fontFamily:t.fontFamily,fontWeight:t.fontWeightNormal,fontSize:t.fontSizeSmall,padding:n.small}}
var C,T,F,_,N,I
var R={componentId:"eZLSb",template:function(e){return"\n\n.eZLSb_bGBk{box-sizing:border-box;display:block;font-family:".concat(e.fontFamily||"inherit",";font-size:").concat(e.fontSize||"inherit",";font-weight:").concat(e.fontWeight||"inherit",";padding:").concat(e.padding||"inherit","}")},root:"eZLSb_bGBk"}
var q=(C=Object(b["a"])(),T=Object(O["a"])(),F=Object(v["i"])(S,R),C(_=T(_=F(_=(I=N=function(e){Object(u["a"])(t,e)
function t(){var e
var n
Object(r["a"])(this,t)
for(var o=arguments.length,a=new Array(o),u=0;u<o;u++)a[u]=arguments[u]
n=Object(i["a"])(this,(e=Object(s["a"])(t)).call.apply(e,[this].concat(a)))
n._id=Object(h["a"])("Tooltip")
return n}Object(a["a"])(t,[{key:"renderTrigger",value:function(e){var n=this.props,o=n.children,r=n.as
var a={"aria-describedby":this._id}
if(r){var i=Object(g["a"])(t,this.props)
var s=Object(j["a"])(this.props,t.propTypes)
return f.a.createElement(i,Object.assign({},s,a),o)}return"function"===typeof o?o({focused:e,getTriggerProps:function(e){return Object(m["a"])({},a,{},e)}}):Object(L["a"])(this.props.children,a)}},{key:"render",value:function(){var e=this
var t=this.props,n=t.renderTip,r=t.isShowingContent,a=t.defaultIsShowingContent,i=t.on,s=t.placement,u=t.color,c=t.mountNode,l=t.constrain,d=t.offsetX,p=t.offsetY,h=t.onRequestShowContent,v=t.onRequestHideContent,b=Object(o["a"])(t,["renderTip","isShowingContent","defaultIsShowingContent","on","placement","color","mountNode","constrain","offsetX","offsetY","onRequestShowContent","onRequestHideContent"])
return f.a.createElement(y["a"],{render:function(t){var o=t.focused
return f.a.createElement(w["a"],Object.assign({},Object(j["b"])(b),{isShowingContent:r,defaultIsShowingContent:a,on:i,shouldRenderOffscreen:true,shouldReturnFocus:false,placement:s,color:"primary"===u?"primary-inverse":"primary",mountNode:c,constrain:l,shadow:"none",offsetX:d,offsetY:p,renderTrigger:function(){return e.renderTrigger(o)},onRequestShowContent:h,onRequestHideContent:v,__dangerouslyIgnoreExperimentalWarnings:true}),f.a.createElement("span",{id:e._id,className:R.root,role:"tooltip"},Object(k["a"])(n)))}})}}])
t.displayName="Tooltip"
return t}(c["Component"]),N.propTypes={children:d.a.oneOfType([d.a.node,d.a.func]).isRequired,renderTip:d.a.oneOfType([d.a.node,d.a.func]).isRequired,isShowingContent:d.a.bool,defaultIsShowingContent:d.a.bool,as:d.a.elementType,on:d.a.oneOfType([d.a.oneOf(["click","hover","focus"]),d.a.arrayOf(d.a.oneOf(["click","hover","focus"]))]),color:d.a.oneOf(["primary","primary-inverse"]),placement:p["a"].placement,mountNode:p["a"].mountNode,constrain:p["a"].constrain,offsetX:d.a.oneOfType([d.a.string,d.a.number]),offsetY:d.a.oneOfType([d.a.string,d.a.number]),onRequestShowContent:d.a.func,onRequestHideContent:d.a.func},N.defaultProps={isShowingContent:void 0,defaultIsShowingContent:false,on:void 0,color:"primary",placement:"top",mountNode:null,constrain:"window",offsetX:0,offsetY:0,onRequestShowContent:function(e){},onRequestHideContent:function(e,t){t.documentClick}},I))||_)||_)||_)
var E=function(e){var t=e.typography,n=e.spacing
return{fontFamily:t.fontFamily,fontWeight:t.fontWeightNormal,fontSize:t.fontSizeSmall,padding:n.small}}
n.d(t,"a",(function(){return J}))
var B,M,x,W,z
var G={componentId:"eZLSb",template:function(e){return"\n\n.eZLSb_bGBk{box-sizing:border-box;display:block;font-family:".concat(e.fontFamily||"inherit",";font-size:").concat(e.fontSize||"inherit",";font-weight:").concat(e.fontWeight||"inherit",";padding:").concat(e.padding||"inherit","}")},root:"eZLSb_bGBk"}
var J=(B=Object(b["a"])(),M=Object(v["i"])(E,G),B(x=M(x=(z=W=function(e){Object(u["a"])(t,e)
function t(){var e
var n
Object(r["a"])(this,t)
for(var o=arguments.length,a=new Array(o),u=0;u<o;u++)a[u]=arguments[u]
n=Object(i["a"])(this,(e=Object(s["a"])(t)).call.apply(e,[this].concat(a)))
n._id=Object(h["a"])("Tooltip")
return n}Object(a["a"])(t,[{key:"render",value:function(){var e=this.props,t=e.children,n=e.tip,r=e.variant,a=e.on,i=e.placement,s=e.mountNode,u=e.constrain,c=Object(o["a"])(e,["children","tip","variant","on","placement","mountNode","constrain"])
return f.a.createElement(q,Object.assign({},c,{renderTip:n,on:a,color:"inverse"===r?"primary":"primary-inverse",placement:i,mountNode:s,constrain:u}),t)}}])
t.displayName="Tooltip"
return t}(c["Component"]),W.propTypes={children:d.a.oneOfType([d.a.node,d.a.func]).isRequired,tip:d.a.node.isRequired,as:d.a.elementType,on:d.a.oneOfType([d.a.oneOf(["click","hover","focus"]),d.a.arrayOf(d.a.oneOf(["click","hover","focus"]))]),variant:d.a.oneOf(["default","inverse"]),placement:p["a"].placement,mountNode:p["a"].mountNode,constrain:p["a"].constrain},W.defaultProps={on:void 0,variant:"inverse",placement:"top",mountNode:null,constrain:"window"},z))||x)||x)},PJ1B:function(e,t,n){"use strict"
var o=n("1OyB")
var r=n("vuIU")
var a=n("md7G")
var i=n("foSv")
var s=n("Ji7U")
n("DEX3")
var u=n("q1tI")
var c=n("17x9")
var f=n.n(c)
var l=n("yfCu")
var d=n("i/8D")
var p={keyboard:"keyboard",pointer:"pointer"}
var h=[]
var v=[]
var b=p.keyboard
var m=0
var y={}
var O=function(e){if("html"===e.target.nodeName.toLowerCase())return
g(b,p.pointer)
h.forEach((function(e){return e.remove()}))}
var g=function(e,t){if(e===t)return
b=t
Object.keys(y).forEach((function(n){return y[n](e,t)}))}
var j=function(){g(b,p.keyboard)}
var L=function(){g(b,p.pointer)}
var k=function(){if(0===h.length){h.push(Object(l["a"])(document,"mousemove",O,true))
h.push(Object(l["a"])(document,"mousedown",O,true))
h.push(Object(l["a"])(document,"mouseup",O,true))
h.push(Object(l["a"])(document,"pointermove",O,true))
h.push(Object(l["a"])(document,"pointerdown",O,true))
h.push(Object(l["a"])(document,"pointerup",O,true))
h.push(Object(l["a"])(document,"touchmove",O,true))
h.push(Object(l["a"])(document,"touchstart",O,true))
h.push(Object(l["a"])(document,"touchend",O,true))}}
var w=function(){if(0===v.length){v.push(Object(l["a"])(document,"keydown",j,true))
v.push(Object(l["a"])(document,"mousedown",L,true))
v.push(Object(l["a"])(document,"pointerdown",L,true))
v.push(Object(l["a"])(document,"touchstart",L,true))}}
var S=function(){h.forEach((function(e){return e.remove()}))
h=[]
v.forEach((function(e){return e.remove()}))
v=[]}
var C=function(e){var t=e.onInputModeChange
var n=m++
"function"===typeof t&&(y[n]=t)
if(d["a"]){w()
k()}return{isKeyboardMode:function(){return b===p.keyboard},remove:function(){1===m&&S()
delete y[n]
m--}}}
var T=n("K7t/")
var F=n("cFoZ")
n.d(t,"a",(function(){return _}))
var _=function(e){Object(s["a"])(t,e)
function t(){var e
var n
Object(o["a"])(this,t)
for(var r=arguments.length,s=new Array(r),u=0;u<r;u++)s[u]=arguments[u]
n=Object(a["a"])(this,(e=Object(i["a"])(t)).call.apply(e,[this].concat(s)))
n._focusListener=null
n._blurListener=null
n._inputModeListener=null
n.state={focused:false,focusable:false}
n.handleInputModeChange=function(){n.forceUpdate()}
n.handleFocus=function(e){n.removeFocusListener()
n.setState({focused:true})}
n.handleBlur=function(e){n.removeBlurListener()
n.setState({focused:false})}
return n}Object(r["a"])(t,[{key:"componentDidMount",value:function(){var e=this.focusable,t=this.focused
this.addFocusableListeners(e,t)
this._inputModeListener=C({onInputModeChange:this.handleInputModeChange})
this.setState({focusable:e,focused:t})}},{key:"componentWillReceiveProps",value:function(e){var t=this.props,n=t.render,o=t.children
e.children===o&&e.render===n||this.removeFocusableListeners()}},{key:"componentDidUpdate",value:function(e,t){var n=this.focusable
if(!n&&this.state.focusable){this.removeFocusableListeners()
this.setState({focusable:false,focused:false})}else if(n!==this.state.focusable){this.removeFocusableListeners()
this.state.focused&&n.focus()
this.addFocusableListeners(n,this.state.focused)
this.setState({focusable:n})}else t.focused!==this.state.focused&&this.addFocusableListeners(n,this.state.focused)}},{key:"componentWillUnmount",value:function(){if(this._inputModeListener){this._inputModeListener.remove()
this._inputModeListener=null}this.removeFocusableListeners()}},{key:"addFocusableListeners",value:function(e,t){if(!e)return
t?this._blurListener=Object(l["a"])(e,"blur",this.handleBlur,true):this._focusListener=Object(l["a"])(e,"focus",this.handleFocus,true)}},{key:"removeFocusableListeners",value:function(){this.removeFocusListener()
this.removeBlurListener()}},{key:"removeFocusListener",value:function(){if(this._focusListener){this._focusListener.remove()
this._focusListener=null}}},{key:"removeBlurListener",value:function(){if(this._blurListener){this._blurListener.remove()
this._blurListener=null}}},{key:"focus",value:function(){var e=this.focusable
e&&e.focus()}},{key:"isFocusVisible",value:function(e,n){if(!e||!n)return false
if(this._inputModeListener&&this._inputModeListener.isKeyboardMode())return true
var o=e.tagName,r=e.type,a=e.isContentEditable
if("INPUT"==o&&t.inputTypes[r])return true
if("TEXTAREA"==o)return true
if(a)return true
return false}},{key:"render",value:function(){var e=this.props,t=e.children,n=e.render,o=void 0===n?t:n
var r=this.state,a=r.focusable,i=r.focused
return"function"===typeof o?o({focused:i,focusable:a,focusVisible:this.isFocusVisible(a,i)}):null}},{key:"focused",get:function(){return Object(T["a"])(this)}},{key:"focusable",get:function(){var e=Object(F["a"])(this,(function(){return true}),true)||[]
var t=e&&e.length||0
"[Focusable] Exactly one focusable child is required (".concat(t," found).")
e=!!e&&e[0]
return!(!e||"function"!==typeof e.focus)&&e}},{key:"focusVisible",get:function(){var e=this.state,t=e.focusable,n=e.focused
return this.isFocusVisible(t,n)}}])
t.displayName="Focusable"
return t}(u["Component"])
_.propTypes={children:f.a.func,render:f.a.func}
_.defaultProps={children:null,render:void 0}
_.inputTypes={text:true,search:true,url:true,tel:true,email:true,password:true,number:true,date:true,month:true,week:true,time:true,datetime:true,"datetime-local":true}}}])

//# sourceMappingURL=14-c-09c47521f2.js.map