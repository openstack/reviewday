// sorttable/sorttable-min.js

var SORT_COLUMN_INDEX;var arrowUp="arrowUp";var arrowDown="arrowDown";var arrowBlank="arrowBlank";function trim(str){return str.replace(/^\s*|\s*$/g,"");}
function sortables_init(){if(!document.getElementsByTagName)return;tbls=document.getElementsByTagName("table");for(ti=0;ti<tbls.length;ti++){thisTbl=tbls[ti];if(((' '+thisTbl.className+' ').indexOf(" sortable ")!=-1)&&(thisTbl.id)){ts_makeSortable(thisTbl);}}}
function ts_makeSortable(table){if(table.tHead&&table.tHead.rows&&table.tHead.rows.length>0){var firstRow=table.tHead.rows[0];}else if(table.rows&&table.rows.length>0){var firstRow=table.rows[0];}
if(!firstRow)return;for(var i=0;i<firstRow.cells.length;i++){var cell=firstRow.cells[i];var txt=ts_getInnerText(cell);cell.innerHTML='<a href="#" class="sortheader" onclick="ts_resortTable(this); return false;">'
+txt+'<img class="sortarrow" src="'+arrowBlank+'" height="6" width="9"></a>';}
for(var i=0;i<firstRow.cells.length;i++){var cell=firstRow.cells[i];var lnk=ts_firstChildByName(cell,'A');var img=ts_firstChildByName(lnk,'IMG')
if((' '+cell.className+' ').indexOf(" default-sort ")!=-1){ts_arrowDown(img);}
if((' '+cell.className+' ').indexOf(" default-revsort ")!=-1){ts_arrowUp(img);}
if((' '+cell.className+' ').indexOf(" initial-sort ")!=-1){ts_resortTable(lnk);}}}
function ts_getInnerText(el){if(typeof el=="string")return el;if(typeof el=="undefined"){return el};/*if(el.innerText)return el.innerText*/;var str="";var cs=el.childNodes;var l=cs.length;for(var i=0;i<l;i++){node=cs[i];switch(node.nodeType){case 1:if(node.className=="sortkey"){return ts_getInnerText(node);}else if(node.className=="revsortkey"){return"-"+ts_getInnerText(node);}else{str+=ts_getInnerText(node);break;}
case 3:str+=node.nodeValue;break;}}
return str;}
function ts_firstChildByName(el,name){for(var ci=0;ci<el.childNodes.length;ci++){if(el.childNodes[ci].tagName&&el.childNodes[ci].tagName.toLowerCase()==name.toLowerCase())
return el.childNodes[ci];}}
function ts_arrowUp(img){img.setAttribute('sortdir','up');img.src=arrowUp;}
function ts_arrowDown(img){img.setAttribute('sortdir','down');img.src=arrowDown;}
function ts_resortTable(lnk){var img=ts_firstChildByName(lnk,'IMG')
var td=lnk.parentNode;var column=td.cellIndex;var table=getParent(td,'TABLE');if(table.rows.length<=1)return;SORT_COLUMN_INDEX=column;while(td.previousSibling!=null){td=td.previousSibling;if(td.nodeType!=1){continue}
colspan=td.getAttribute("colspan");if(colspan){SORT_COLUMN_INDEX+=parseInt(colspan)-1;}}
var itm=ts_getInnerText(table.rows[1].cells[SORT_COLUMN_INDEX]);itm=trim(itm);sortfn=ts_sort_caseinsensitive;if(itm.match(/^\d\d[\/-]\d\d[\/-]\d\d\d\d$/))sortfn=ts_sort_date;if(itm.match(/^\d\d[\/-]\d\d[\/-]\d\d$/))sortfn=ts_sort_date;if(itm.match(/^[£$]/))sortfn=ts_sort_currency;if(itm.match(/^-?[\d\.]+$/))sortfn=ts_sort_numeric;var firstRow=new Array();var newRows=new Array();for(i=0;i<table.rows[0].length;i++){firstRow[i]=table.rows[0][i];}
for(j=1;j<table.rows.length;j++){newRows[j-1]=table.rows[j];newRows[j-1].oldPosition=j-1;}
newRows.sort(ts_stableSort(sortfn));if(img.getAttribute("sortdir")=='down'){newRows.reverse();ts_arrowUp(img);}else{ts_arrowDown(img);}
for(i=0;i<newRows.length;i++){if(!newRows[i].className||(newRows[i].className&&(newRows[i].className.indexOf('sortbottom')==-1)))
table.tBodies[0].appendChild(newRows[i]);}
for(i=0;i<newRows.length;i++){if(newRows[i].className&&(newRows[i].className.indexOf('sortbottom')!=-1))
table.tBodies[0].appendChild(newRows[i]);}
var allimgs=document.getElementsByTagName("img");for(var ci=0;ci<allimgs.length;ci++){var one_img=allimgs[ci];if(one_img!=img&&one_img.className=='sortarrow'&&getParent(one_img,"table")==getParent(lnk,"table")){one_img.src=arrowBlank;one_img.setAttribute('sortdir','');}}}
function getParent(el,pTagName){if(el==null)
return null;else if(el.nodeType==1&&el.tagName.toLowerCase()==pTagName.toLowerCase())
return el;else
return getParent(el.parentNode,pTagName);}
function ts_stableSort(sortfn){function stableSort(a,b){var cmp=sortfn(a,b);if(cmp!=0){return cmp;}else{return a.oldPosition-b.oldPosition;}}
return stableSort;}
function ts_sort_date(a,b){aa=trim(ts_getInnerText(a.cells[SORT_COLUMN_INDEX]));bb=trim(ts_getInnerText(b.cells[SORT_COLUMN_INDEX]));if(aa.length==10){dt1=aa.substr(6,4)+aa.substr(3,2)+aa.substr(0,2);}else{yr=aa.substr(6,2);if(parseInt(yr)<50){yr='20'+yr;}else{yr='19'+yr;}
dt1=yr+aa.substr(3,2)+aa.substr(0,2);}
if(bb.length==10){dt2=bb.substr(6,4)+bb.substr(3,2)+bb.substr(0,2);}else{yr=bb.substr(6,2);if(parseInt(yr)<50){yr='20'+yr;}else{yr='19'+yr;}
dt2=yr+bb.substr(3,2)+bb.substr(0,2);}
if(dt1==dt2)return 0;if(dt1<dt2)return-1;return 1;}
function ts_sort_currency(a,b){aa=ts_getInnerText(a.cells[SORT_COLUMN_INDEX]).replace(/[^0-9.]/g,'');bb=ts_getInnerText(b.cells[SORT_COLUMN_INDEX]).replace(/[^0-9.]/g,'');return parseFloat(aa)-parseFloat(bb);}
function ts_sort_numeric(a,b){aa=parseFloat(ts_getInnerText(a.cells[SORT_COLUMN_INDEX]));if(isNaN(aa))aa=0;bb=parseFloat(ts_getInnerText(b.cells[SORT_COLUMN_INDEX]));if(isNaN(bb))bb=0;return aa-bb;}
function ts_sort_caseinsensitive(a,b){aa=ts_getInnerText(a.cells[SORT_COLUMN_INDEX]).toLowerCase();bb=ts_getInnerText(b.cells[SORT_COLUMN_INDEX]).toLowerCase();if(aa==bb)return 0;if(aa<bb)return-1;return 1;}
function ts_sort_default(a,b){aa=ts_getInnerText(a.cells[SORT_COLUMN_INDEX]);bb=ts_getInnerText(b.cells[SORT_COLUMN_INDEX]);if(aa==bb)return 0;if(aa<bb)return-1;return 1;}
function addEvent(elm,evType,fn,useCapture){if(elm.addEventListener){elm.addEventListener(evType,fn,useCapture);return true;}else if(elm.attachEvent){var r=elm.attachEvent("on"+evType,fn);return r;}else{alert("Handler could not be removed");}}
