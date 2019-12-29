(window["canvasWebpackJsonp"]=window["canvasWebpackJsonp"]||[]).push([[69],{BHWx:function(e,i,t){"use strict"
t.r(i)
var a=t("ODXe")
var l=t("mNVu")
var _=t("Cf7h")
const n=ENV.FILES_CONTEXTS||[]
const s={contexts:n,contextsDictionary:n.reduce((e,i)=>{const t=Array.from(Object(_["a"])(i.asset_string)),l=Object(a["a"])(t,2),n=l[0],s=l[1]
i.contextType=n
i.contextId=s
e[[n,s].join("_")]=i
return e},{}),showingAllContexts:window.location.pathname.match(/^\/files/),contextType:null!=n[0]?n[0].contextType:void 0,contextId:null!=n[0]?n[0].contextId:void 0,rootFolders:n.map(e=>{if(ENV.current_user_id){const i=new l["a"]({custom_name:e.name,context_type:e.contextType.replace(/s$/,""),context_id:e.contextId})
i.url="/api/v1/".concat(e.contextType,"/").concat(e.contextId,"/folders/root")
i.fetch()
return i}})}
s.contextFor=function(e){let i
e.collection&&e.collection.parentFolder&&(e=e.collection.parentFolder)
if(e instanceof l["a"]){const t=e
i="".concat(t&&t.get("context_type"),"s_").concat(t&&t.get("context_id")).toLowerCase()}else e.contextType&&e.contextId&&(i="".concat(e.contextType,"_").concat(e.contextId).toLowerCase())
return s.contextsDictionary&&s.contextsDictionary[i]}
s.userHasPermission=function(e,i){if(!e)return false
return s.contextFor(e)&&s.contextFor(e).permissions&&s.contextFor(e).permissions[i]}
s.baseUrl=s.showingAllContexts?"/files":"/".concat(s.contextType,"/").concat(s.contextId,"/files")
i["default"]=s},"Ewk/":function(e,i,t){"use strict"
var a=t("An8g")
var l=t("q1tI")
var _=t.n(l)
var n=t("fhzG")
var s=t.n(n)
var o=t("i8i4")
var r=t.n(o)
var c=t("ouhR")
var d=t.n(c)
var f=t("pQTu")
var u=t("m0r6")
Object(u["a"])(JSON.parse('{"ar":{"editing_permissions_for_name_3503e235":"أذونات التحرير لصالح: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} غير ظاهر في ملفات الطالب - انقر للتعديل","filename_is_published_click_to_modify_38a4a269":"%{fileName} منشور - انقر للتعديل","filename_is_restricted_9aaf9250":"%{fileName} - %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName}  %{restricted} - انقر للتعديل","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} غير منشور - انقر للتعديل","not_visible_in_student_files_22f11883":"غير مرئي في ملفات الطالب","published_4bb5209e":"تم النشر","this_file_9443cda1":"هذا الملف","unpublished_8b6107d6":"غير منشور"},"cy":{"editing_permissions_for_name_3503e235":"Golygu hawliau ar gyfer: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"Dydy %{fileName} ddim yn ymddangos mewn ffeiliau myfyrwyr – Cliciwch i addasu hyn","filename_is_published_click_to_modify_38a4a269":"%{fileName} wedi Cyhoeddi - Cliciwch i addasu","filename_is_restricted_9aaf9250":"%{fileName} yn %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} %{restricted} - Cliciwch i addasu","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} heb Gyhoeddi - Cliciwch i addasu","not_visible_in_student_files_22f11883":"Ddim yn ymddangos mewn ffeiliau myfyrwyr","published_4bb5209e":"Wedi cyhoeddi","this_file_9443cda1":"Mae’r ffeil hon","unpublished_8b6107d6":"Heb gyhoeddi"},"da":{"editing_permissions_for_name_3503e235":"Redigerer tilladelser til: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} er ikke synligt i filer for studerende - Klik for at ændre","filename_is_published_click_to_modify_38a4a269":"%{fileName} er offentliggjort, klik for at ændre","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted}, klik for at ændre","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er ikke offentliggjort, klik for at ændre","not_visible_in_student_files_22f11883":"Ikke synlig i filer for studerende","published_4bb5209e":"Offentliggjort","this_file_9443cda1":"Denne fil","unpublished_8b6107d6":"Ikke offentliggjort"},"da-x-k12":{"editing_permissions_for_name_3503e235":"Redigerer tilladelser til: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} er offentliggjort, klik for at ændre","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted}, klik for at ændre","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er ikke offentliggjort, klik for at ændre","published_4bb5209e":"Offentliggjort","this_file_9443cda1":"Denne fil","unpublished_8b6107d6":"Ikke offentliggjort"},"de":{"editing_permissions_for_name_3503e235":"Änderungsberechtigungen für: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} ist in Studentendateien nicht sichtbar – Um das zu ändern, hier klicken","filename_is_published_click_to_modify_38a4a269":"%{fileName} ist veröffentlicht – zum Ändern anklicken","filename_is_restricted_9aaf9250":"%{fileName} ist %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} Ist %{restricted} – zum Ändern klicken","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Ist nicht veröffentlicht – zum Ändern anklicken","not_visible_in_student_files_22f11883":"In Studentendateien nicht sichtbar.","published_4bb5209e":"Veröffentlicht","this_file_9443cda1":"Diese Datei","unpublished_8b6107d6":"Nicht veröffentlicht"},"el":{"editing_permissions_for_name_3503e235":"\\u003cmrk mid=\\"7571\\" mtype=\\"seg\\"\\u003eΆδειες επεξεργασίας για:\\u003c/mrk\\u003e \\u003cmrk mid=\\"7572\\" mtype=\\"seg\\"\\u003e%{name}\\u003c/mrk\\u003e","published_4bb5209e":"Δημοσιευμένο/α","this_file_9443cda1":"Αυτό το αρχείο","unpublished_8b6107d6":"Μη δημοσιευμένο"},"en-AU":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is not visible in student files - Click to modify","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","not_visible_in_student_files_22f11883":"Not visible in student files","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"en-AU-x-unimelb":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is not visible in student files - Click to modify","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","not_visible_in_student_files_22f11883":"Not visible in student files","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"en-CA":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is not visible in student files - Click to modify","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","not_visible_in_student_files_22f11883":"Not visible in student files","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"en-GB":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is not visible in student files - Click to modify","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","not_visible_in_student_files_22f11883":"Not visible in student files","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"en-GB-x-lbs":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"en-GB-x-ukhe":{"editing_permissions_for_name_3503e235":"Editing permissions for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is not visible in student files - Click to modify","filename_is_published_click_to_modify_38a4a269":"%{fileName} is Published - Click to modify","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Click to modify","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is Unpublished - Click to modify","not_visible_in_student_files_22f11883":"Not visible in student files","published_4bb5209e":"Published","this_file_9443cda1":"This file","unpublished_8b6107d6":"Unpublished"},"es":{"editing_permissions_for_name_3503e235":"Editando permisos para: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} no es visible en los archivos de los alumnos. Haga clic para modificar","filename_is_published_click_to_modify_38a4a269":"%{fileName} está publicado: Haga clic para modificar","filename_is_restricted_9aaf9250":"%{fileName} es %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} está %{restricted}: Haga clic para modificar","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} no está publicado: Haga clic para modificar","not_visible_in_student_files_22f11883":"No visible en los archivos de los alumnos","published_4bb5209e":"Publicado","this_file_9443cda1":"Este archivo","unpublished_8b6107d6":"No publicado"},"fa":{"editing_permissions_for_name_3503e235":"مجوزهای ویرایش برای: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} منتشر شده است. برای تغییر کلیک کنید","filename_is_restricted_9aaf9250":"%{fileName} %{restricted} است","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} %{restricted}است- برای تغییر کلیک کنید","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} منتشر نشده است. برای تغییر کلیک کنید","published_4bb5209e":"منتشر شده","this_file_9443cda1":"این فایل","unpublished_8b6107d6":"منتشر نشده"},"fi":{"editing_permissions_for_name_3503e235":"Muokataan käyttöoikeuksia kohteelle: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} ei ole näkyvissä opiskelijatiedostoille - Muokkaa napsauttamalla","filename_is_published_click_to_modify_38a4a269":"%{fileName} On julkaistu - Napsauta muokataksesi","filename_is_restricted_9aaf9250":"%{fileName} on %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} on %{restricted} - Napsauta muokkaa","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Julkaisu on kumottu - Napsauta muokataksesi","not_visible_in_student_files_22f11883":"Ei näkyvillä opiskelijan tiedostoissa","published_4bb5209e":"Julkaistu","this_file_9443cda1":"Tämä tiedosto","unpublished_8b6107d6":"Julkaisematon"},"fr":{"editing_permissions_for_name_3503e235":"Modifier les autorisations de : %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} N’est pas visible parmi les fichiers des élèves - Cliquez pour modifier.","filename_is_published_click_to_modify_38a4a269":"%{fileName} est publié – Cliquez pour modifier","filename_is_restricted_9aaf9250":"%{fileName} est %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} est %{restricted} – Cliquez pour modifier","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} n’est pas publié – Cliquez pour modifier","not_visible_in_student_files_22f11883":"Non visible dans les fichiers des élèves","published_4bb5209e":"Publié","this_file_9443cda1":"Ce fichier","unpublished_8b6107d6":"Non publié(e)(s)"},"fr-CA":{"editing_permissions_for_name_3503e235":"Modifier les autorisations de : %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} est non visible dans les fichiers des étudiants - Cliquez pour modifier","filename_is_published_click_to_modify_38a4a269":"%{fileName} Est publié - Cliquez pour modifier","filename_is_restricted_9aaf9250":"%{fileName} est %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} Est %{restricted} - Cliquez pour modifier","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Est non publié - Cliquez pour modifier","not_visible_in_student_files_22f11883":"Non visible dans les fichiers de l’étudiant","published_4bb5209e":"Date de publication","this_file_9443cda1":"Ce fichier","unpublished_8b6107d6":"Non publié"},"he":{"editing_permissions_for_name_3503e235":"עריכת הרשאות ל: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} פורסם. - הקש/י כדי לעדכן","filename_is_restricted_9aaf9250":"%{fileName} הנו%{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} הנו %{restricted} - הקש/י כדי לעדכן","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} טרם פורסם - הקש/י כדי לעדכן","published_4bb5209e":"פורסם","this_file_9443cda1":"קובץ זה","unpublished_8b6107d6":"לא פורסם"},"ht":{"editing_permissions_for_name_3503e235":"Modifikasyon pèmisyon pou: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} pa vizib nan fichye elèv yo - Klike pou ka chanje","filename_is_published_click_to_modify_38a4a269":"%{fileName} Pibliye - Klike pou modifye","filename_is_restricted_9aaf9250":"%{fileName} se %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} se %{restricted} - Klike pou modifye","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Pa pibliye - Klike pou modifye","not_visible_in_student_files_22f11883":"Pa vizib nan fichye elèv yo","published_4bb5209e":"Pibliye","this_file_9443cda1":"Fichye sa a","unpublished_8b6107d6":"Pa Pibliye"},"hu":{"editing_permissions_for_name_3503e235":"%{name} jogainak szerkesztése","published_4bb5209e":"Publikált","this_file_9443cda1":"Ez a fájl","unpublished_8b6107d6":"Nem publikált"},"hy":{"editing_permissions_for_name_3503e235":"Խմբագրման թույլտվություն %{name}-ի համար","published_4bb5209e":"Հրապարակված","this_file_9443cda1":"Այս ֆայլը","unpublished_8b6107d6":"Չհրապարակված"},"is":{"editing_permissions_for_name_3503e235":"Breyta heimildum fyrir: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} er ekki sýnilegt í skrám nemanda - smelltu til að breyta","filename_is_published_click_to_modify_38a4a269":"%{fileName} er birt - Smelltu til að breyta","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted} - Smelltu til að breyta","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er óbirt - Smelltu til að breyta","not_visible_in_student_files_22f11883":"Ekki sýnilegt í skrám nemanda","published_4bb5209e":"Birt","this_file_9443cda1":"Þessi skrá","unpublished_8b6107d6":"Óbirt"},"it":{"editing_permissions_for_name_3503e235":"Modifica autorizzazioni per: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} non è visibile nei file studente - Fare clic per modificare","filename_is_published_click_to_modify_38a4a269":"%{fileName} è pubblicato - Fai clic per modificare","filename_is_restricted_9aaf9250":"%{fileName} è %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} è %{restricted} - Fai clic per modificare","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} non è pubblicato - Fai clic per modificare","not_visible_in_student_files_22f11883":"Non visibile nei file degli studenti","published_4bb5209e":"Pubblicato","this_file_9443cda1":"Questo file","unpublished_8b6107d6":"Non pubblicato"},"ja":{"editing_permissions_for_name_3503e235":"編集権限: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName}は、受講生のファイルには表示されません - クリックして変更します","filename_is_published_click_to_modify_38a4a269":"%{fileName} 公開されています - クリックして修正する","filename_is_restricted_9aaf9250":"%{fileName} は%{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} %{restricted} - クリックして変更","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} 非公開となっています - クリックして変更","not_visible_in_student_files_22f11883":"受講生ファイルでは表示できません。","published_4bb5209e":"公開済み","this_file_9443cda1":"このファイル","unpublished_8b6107d6":"未公開"},"mi":{"editing_permissions_for_name_3503e235":"Whakatika whakāetanga mō: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} kaore e kitea i roto i ngā ākonga kōnae Pāwhiri ki te whakamahi","filename_is_published_click_to_modify_38a4a269":"%{fileName} Kei te whakaputaina - Pāwhiritia ki te whakarerekē","filename_is_restricted_9aaf9250":"%{fileName} ko %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} Ko %{restricted} Pāwhiritia ki te whakarerekē","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Kua kore e whakaputaina - Pāwhiritia ki te whakarerekē","not_visible_in_student_files_22f11883":"Kaore i kites i roto i ngā ākonga kōnae","published_4bb5209e":"I whakaputaina","this_file_9443cda1":"tēnei kōnae","unpublished_8b6107d6":"Kaore i"},"nb":{"editing_permissions_for_name_3503e235":"Redigerer rettigheter for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} er ikke synlig i studentfiler - klikk for å endre","filename_is_published_click_to_modify_38a4a269":"%{fileName} er publisert - Klikk for å endre","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted} - Klikk for å endre","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er upublisert - Klikk for å endre","not_visible_in_student_files_22f11883":"Ikke synlig i studentfiler","published_4bb5209e":"Publisert","this_file_9443cda1":"denne filen","unpublished_8b6107d6":"Ikke publisert"},"nb-x-k12":{"editing_permissions_for_name_3503e235":"Redigerer rettigheter for: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} er publisert - Klikk for å endre","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted} - Klikk for å endre","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er upublisert - Klikk for å endre","published_4bb5209e":"Publisert","this_file_9443cda1":"denne filen","unpublished_8b6107d6":"Ikke publisert"},"nl":{"editing_permissions_for_name_3503e235":"Vergunningen bewerken voor: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} is niet zichtbaar in cursistbestanden - Klik om te wijzigen","filename_is_published_click_to_modify_38a4a269":"%{fileName} is gepubliceerd - Klik om te wijzigen","filename_is_restricted_9aaf9250":"%{fileName} is %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} is %{restricted} - Klik om te wijzigen","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} is niet gepubliceerd - Klik om te wijzigen","not_visible_in_student_files_22f11883":"Niet zichtbaar in cursistbestanden.","published_4bb5209e":"Gepubliceerd","this_file_9443cda1":"Dit bestand","unpublished_8b6107d6":"Niet-gepubliceerd"},"nn":{"editing_permissions_for_name_3503e235":"Rediger løyve for: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} er ikkje synleg i studentfiler - klikk for å endre","filename_is_published_click_to_modify_38a4a269":"%{fileName} er publisert - klikk for å endre","filename_is_restricted_9aaf9250":"%{fileName} er %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} er %{restricted} - klikk for å endre","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} er upublisert - klikk for å endre","not_visible_in_student_files_22f11883":"Ikkje synleg i studentfiler","published_4bb5209e":"Publisert","this_file_9443cda1":"Denne fila","unpublished_8b6107d6":"Ikkje publisert"},"pl":{"editing_permissions_for_name_3503e235":"Uprawnienia do edycji posiada: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} nie jest widoczna w plikach uczestnikach – Kliknij, aby zmienić","filename_is_published_click_to_modify_38a4a269":"%{fileName} jest opublikowany – kliknij, aby zmienić.","filename_is_restricted_9aaf9250":"%{fileName} jest %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} jest %{restricted} – kliknij, aby zmienić.","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} jest nieopublikowany – kliknij, aby zmienić.","not_visible_in_student_files_22f11883":"Niewidoczne w plikach uczestników","published_4bb5209e":"Opublikowane","this_file_9443cda1":"Ten plik","unpublished_8b6107d6":"Nieopublikowane"},"pt":{"editing_permissions_for_name_3503e235":"Permissões de edição para: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} não está visível nos ficheiros dos alunos - Clique para modificar","filename_is_published_click_to_modify_38a4a269":"%{fileName} Está publicado - Clique para modificar","filename_is_restricted_9aaf9250":"%{fileName} Está %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} Está %{restricted} - Clique para modificar","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Não está publicado - Clique para modificar","not_visible_in_student_files_22f11883":"Não visível nos ficheiros dos alunos","published_4bb5209e":"Publicado","this_file_9443cda1":"Este ficheiro","unpublished_8b6107d6":"Não publicado"},"pt-BR":{"editing_permissions_for_name_3503e235":"Permissões de edição para: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} Não está visível nos arquivos do aluno - Clique para modificar","filename_is_published_click_to_modify_38a4a269":"%{fileName} está publicado - Clique para modificar","filename_is_restricted_9aaf9250":"%{fileName} é %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} está %{restricted} - Clique para modificar","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} não está publicado - Clique para modificar","not_visible_in_student_files_22f11883":"Invisível nos arquivos de alunos","published_4bb5209e":"Publicado","this_file_9443cda1":"Este arquivo","unpublished_8b6107d6":"Não publicado"},"ru":{"editing_permissions_for_name_3503e235":"Редактирование разрешений для: %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} не отображается в файлах учащихся - нажмите для изменения","filename_is_published_click_to_modify_38a4a269":"%{fileName} Опубликован - Нажмите для изменения","filename_is_restricted_9aaf9250":"%{fileName} является %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} является %{restricted} - Нажмите для изменения","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Не опубликован - Нажмите для изменения","not_visible_in_student_files_22f11883":"Не отображается в файлах учащихся","published_4bb5209e":"Опубликовано","this_file_9443cda1":"Этот файл","unpublished_8b6107d6":"Не опубликовано"},"sl":{"editing_permissions_for_name_3503e235":"Urejanje dovoljenj za: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} je objavljeno – kliknite, da prilagodite.","filename_is_restricted_9aaf9250":"%{fileName} je %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} je %{restricted} – kliknite, da prilagodite.","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} je neobjavljeno – kliknite, da prilagodite.","published_4bb5209e":"Objavljeno","this_file_9443cda1":"Ta datoteka","unpublished_8b6107d6":"Neobjavljeno"},"sv":{"editing_permissions_for_name_3503e235":"Redigerar tillstånd för %{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} är inte synlig i studentfiler – Klicka för att ändra","filename_is_published_click_to_modify_38a4a269":"%{fileName} är publicerad - klicka för att modifiera","filename_is_restricted_9aaf9250":"%{fileName} är %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} är %{restricted} - klicka för att modifiera","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Är opublicerad - klicka för att modifiera","not_visible_in_student_files_22f11883":"Ej synlig i studentfiler","published_4bb5209e":"Publicerad","this_file_9443cda1":"Denna filen","unpublished_8b6107d6":"Avpublicerad"},"sv-x-k12":{"editing_permissions_for_name_3503e235":"Redigerar tillstånd för %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} är publicerad - klicka för att modifiera","filename_is_restricted_9aaf9250":"%{fileName} är %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} är %{restricted} - klicka för att modifiera","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} Är opublicerad - klicka för att modifiera","published_4bb5209e":"Publicerad","this_file_9443cda1":"Denna filen","unpublished_8b6107d6":"Avpublicerad"},"tr":{"editing_permissions_for_name_3503e235":"%{name} için izinler düzenleniyor","filename_is_restricted_9aaf9250":"%{fileName}  %{restricted}dir","published_4bb5209e":"Yayınlandı","this_file_9443cda1":"Bu dosya","unpublished_8b6107d6":"Yayınlanmamış"},"uk":{"editing_permissions_for_name_3503e235":"Редагування дозволів для: %{name}","filename_is_published_click_to_modify_38a4a269":"%{fileName} опубліковано - Натисніть, щоб змінити","filename_is_restricted_9aaf9250":"%{fileName} є %{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} є %{restricted} - Натисніть, щоб змінити","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} неопубліковано - Натисніть, щоб змінити","published_4bb5209e":"Опубліковано","this_file_9443cda1":"Цей файл","unpublished_8b6107d6":"Публікацію відмінено"},"zh-Hans":{"editing_permissions_for_name_3503e235":"为%{name}的编辑权限","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName}在学生文件中不显示 - 请点击调整","filename_is_published_click_to_modify_38a4a269":"%{fileName} 已发布 - 单击以修改","filename_is_restricted_9aaf9250":"%{fileName} 是%{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} 是 %{restricted} - 单击以修改","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} 未发布 - 单击以修改","not_visible_in_student_files_22f11883":"在学生文件中不可见","published_4bb5209e":"已发布","this_file_9443cda1":"此文件","unpublished_8b6107d6":"取消发布"},"zh-Hant":{"editing_permissions_for_name_3503e235":"編輯權限：%{name}","filename_is_not_visible_in_student_files_click_to__aa2a0651":"%{fileName} 在學生檔案中無法看到 - 按一下以修改","filename_is_published_click_to_modify_38a4a269":"%{fileName} 已發佈 - 按一下進行修改","filename_is_restricted_9aaf9250":"%{fileName} 是%{restricted}","filename_is_restricted_click_to_modify_c0bb77f8":"%{fileName} 已 %{restricted} - 按一下進行修改","filename_is_unpublished_click_to_modify_7e731102":"%{fileName} 未發佈 - 按一下進行修改","not_visible_in_student_files_22f11883":"在學生檔案中看不到","published_4bb5209e":"已發佈","this_file_9443cda1":"此文儅","unpublished_8b6107d6":"已取消發佈"}}'))
t("jQeR")
t("0sPK")
var b=f["default"].scoped("publish_cloud")
var m=t("17x9")
var p=t.n(m)
Object(u["a"])(JSON.parse('{"ar":{"available_after_unlock_at_b5682224":"متاح بعد %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"متاح بعد %{unlock_at} حتى %{lock_at}","available_until_lock_at_ab022445":"متاح حتى %{lock_at}"},"cy":{"available_after_unlock_at_b5682224":"Ar gael ar ôl %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Ar gael ar ôl %{unlock_at} tan %{lock_at}","available_until_lock_at_ab022445":"Ar gael tan %{lock_at}"},"da":{"available_after_unlock_at_b5682224":"Tilgængelig efter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tilgængelig efter %{unlock_at} indtil %{lock_at}","available_until_lock_at_ab022445":"Tilgængelig til %{lock_at}"},"da-x-k12":{"available_after_unlock_at_b5682224":"Tilgængelig efter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tilgængelig efter %{unlock_at} indtil %{lock_at}","available_until_lock_at_ab022445":"Tilgængelig til %{lock_at}"},"de":{"available_after_unlock_at_b5682224":"Verfügbar von %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Verfügbar von %{unlock_at} bis %{lock_at}","available_until_lock_at_ab022445":"Verfügbar bis %{lock_at}"},"el":{"available_after_unlock_at_b5682224":"Διαθέσιμο μετά από τις %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Διαθέσιμο από τις %{unlock_at} έως τις %{lock_at}","available_until_lock_at_ab022445":"Διαθέσιμο έως τις %{lock_at}"},"en-AU":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"en-AU-x-unimelb":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"en-CA":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"en-GB":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"en-GB-x-lbs":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"en-GB-x-ukhe":{"available_after_unlock_at_b5682224":"Available after %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Available after %{unlock_at} until %{lock_at}","available_until_lock_at_ab022445":"Available until %{lock_at}"},"es":{"available_after_unlock_at_b5682224":"Disponible a partir de %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponible a partir de %{unlock_at} hasta %{lock_at}","available_until_lock_at_ab022445":"Disponible hasta %{lock_at}"},"fa":{"available_after_unlock_at_b5682224":"بعد از %{unlock_at} در دسترس است","available_after_unlock_at_until_lock_at_499e8092":"بعد از %{unlock_at} تا %{lock_at} در دسترس است","available_until_lock_at_ab022445":"تا %{lock_at} قابل دسترسی است"},"fi":{"available_after_unlock_at_b5682224":"Saatavilla %{unlock_at} jälkeen","available_after_unlock_at_until_lock_at_499e8092":"Saatavissa %{unlock_at} jälkeen %{lock_at} asti","available_until_lock_at_ab022445":"Saatavissa asti %{lock_at}"},"fr":{"available_after_unlock_at_b5682224":"Disponible après %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponible après %{unlock_at} et jusqu’à %{lock_at}","available_until_lock_at_ab022445":"Disponible jusqu’à %{lock_at}"},"fr-CA":{"available_after_unlock_at_b5682224":"Disponible après %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponible après %{unlock_at} et jusqu’à %{lock_at}","available_until_lock_at_ab022445":"Disponible jusqu’à %{lock_at}"},"he":{"available_after_unlock_at_b5682224":"זמין אחרי %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"זמין אחרי %{unlock_at}  עד %{lock_at}","available_until_lock_at_ab022445":"זמין עד %{lock_at}"},"ht":{"available_after_unlock_at_b5682224":"Disponib aprè %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponib aprè %{unlock_at} jiska %{lock_at}","available_until_lock_at_ab022445":"Disponib jiska %{lock_at}"},"hu":{"available_after_unlock_at_b5682224":"Elérhető ettől %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Elérhető ettől %{unlock_at}, eddig: %{lock_at}","available_until_lock_at_ab022445":"Elérhető eddig: %{lock_at}"},"hy":{"available_after_unlock_at_b5682224":"Հասանելի է %{unlock_at}-ից հետո","available_after_unlock_at_until_lock_at_499e8092":"Հասանելի է %{unlock_at}-ից հետո մինչև %{lock_at}","available_until_lock_at_ab022445":"Հասանելի է մինչև %{lock_at}"},"is":{"available_after_unlock_at_b5682224":"Tiltækt eftir %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tiltækt eftir %{unlock_at} til %{lock_at}","available_until_lock_at_ab022445":"Tiltækt til %{lock_at}"},"it":{"available_after_unlock_at_b5682224":"Disponibile dopo %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponibile dopo %{unlock_at} fino a %{lock_at}","available_until_lock_at_ab022445":"Disponibile fino a %{lock_at}"},"ja":{"available_after_unlock_at_b5682224":"%{unlock_at} 後に利用可能","available_after_unlock_at_until_lock_at_499e8092":"%{unlock_at} 後に %{lock_at} まで利用可能","available_until_lock_at_ab022445":"%{lock_at} まで利用可能"},"mi":{"available_after_unlock_at_b5682224":"Wātea i muri %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Wātea i muri %{unlock_at} noa %{lock_at}","available_until_lock_at_ab022445":"Wātea noa %{lock_at}"},"nb":{"available_after_unlock_at_b5682224":"Tilgjengelig etter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tilgjengelig etter %{unlock_at} inntil %{lock_at}","available_until_lock_at_ab022445":"Tilgjengelig til %{lock_at}"},"nb-x-k12":{"available_after_unlock_at_b5682224":"Tilgjengelig etter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tilgjengelig etter %{unlock_at} inntil %{lock_at}","available_until_lock_at_ab022445":"Tilgjengelig til %{lock_at}"},"nl":{"available_after_unlock_at_b5682224":"Beschikbaar na %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Beschikbaar na %{unlock_at} en tot en met %{lock_at}","available_until_lock_at_ab022445":"Beschikbaar tot %{lock_at}"},"nn":{"available_after_unlock_at_b5682224":"Tilgjengeleg etter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tilgjengeleg etter %{unlock_at} til %{lock_at}","available_until_lock_at_ab022445":"Tilgjengeleg til %{lock_at}"},"pl":{"available_after_unlock_at_b5682224":"Dostępne po %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Dostępne po %{unlock_at} aż do %{lock_at}","available_until_lock_at_ab022445":"Dostępne do %{lock_at}"},"pt":{"available_after_unlock_at_b5682224":"Disponível após %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponível após %{unlock_at} até %{lock_at}","available_until_lock_at_ab022445":"Disponível até %{lock_at}"},"pt-BR":{"available_after_unlock_at_b5682224":"Disponível após %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Disponível após %{unlock_at} até %{lock_at}","available_until_lock_at_ab022445":"Disponível até %{lock_at}"},"ru":{"available_after_unlock_at_b5682224":"Доступно с %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Доступно с %{unlock_at} до %{lock_at}","available_until_lock_at_ab022445":"Доступно до %{lock_at}"},"sl":{"available_after_unlock_at_b5682224":"Na voljo po %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Na voljo po %{unlock_at} do %{lock_at}","available_until_lock_at_ab022445":"Na voljo do %{lock_at}"},"sv":{"available_after_unlock_at_b5682224":"Tillgänglig efter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tillgänglig efter %{unlock_at} till %{lock_at}","available_until_lock_at_ab022445":"Tillgänglig tills %{lock_at}"},"sv-x-k12":{"available_after_unlock_at_b5682224":"Tillgänglig efter %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Tillgänglig efter %{unlock_at} till %{lock_at}","available_until_lock_at_ab022445":"Tillgänglig tills %{lock_at}"},"tr":{"available_after_unlock_at_b5682224":"%{unlock_at} tarihinden sonra geçerli","available_after_unlock_at_until_lock_at_499e8092":"%{unlock_at} tarihinden sonra %{lock_at} tarihine kadar geçerli","available_until_lock_at_ab022445":"%{lock_at} tarihine kadar geçerli"},"uk":{"available_after_unlock_at_b5682224":"Доступно після %{unlock_at}","available_after_unlock_at_until_lock_at_499e8092":"Доступно після %{unlock_at} до %{lock_at}","available_until_lock_at_ab022445":"Доступно до %{lock_at}"},"zh-Hans":{"available_after_unlock_at_b5682224":"%{unlock_at} 之后可用","available_after_unlock_at_until_lock_at_499e8092":"%{unlock_at} 之后、%{lock_at} 之前可用","available_until_lock_at_ab022445":"%{lock_at} 之前可用"},"zh-Hant":{"available_after_unlock_at_b5682224":"在 %{unlock_at} 之後可用","available_after_unlock_at_until_lock_at_499e8092":"在 %{unlock_at} 之後和 %{lock_at} 之前可用","available_until_lock_at_ab022445":"可用截止時間 %{lock_at}"}}'))
var k=f["default"].scoped("broccoli_cloud")
var h=t("lUQV")
t("MWZS")
t("UlQx")
var v={displayName:"PublishCloud",propTypes:{togglePublishClassOn:p.a.object,model:h["a"].filesystemObject,userCanManageFilesForContext:p.a.bool.isRequired,fileName:p.a.string},getInitialState(){return this.extractStateFromModel(this.props.model)},componentDidMount(){this.props.togglePublishClassOn&&this.updatePublishClassElements()},componentDidUpdate(){this.props.togglePublishClassOn&&this.updatePublishClassElements()},componentWillMount(){const e=e=>this.setState(this.extractStateFromModel(e))
this.props.model.on("change",e,this)},componentWillUnmount(){this.props.model.off(null,null,this)},updatePublishClassElements(){return this.props.togglePublishClassOn.classList[this.state.published?"add":"remove"]("ig-published")},getRestrictedText(){if(this.props.model.get("unlock_at")&&this.props.model.get("lock_at"))return k.t("Available after %{unlock_at} until %{lock_at}",{unlock_at:d.a.datetimeString(this.props.model.get("unlock_at")),lock_at:d.a.datetimeString(this.props.model.get("lock_at"))})
if(this.props.model.get("unlock_at")&&!this.props.model.get("lock_at"))return k.t("Available after %{unlock_at}",{unlock_at:d.a.datetimeString(this.props.model.get("unlock_at"))})
if(!this.props.model.get("unlock_at")&&this.props.model.get("lock_at"))return k.t("Available until %{lock_at}",{lock_at:d.a.datetimeString(this.props.model.get("lock_at"))})},extractStateFromModel:e=>({published:!e.get("locked"),restricted:!!e.get("lock_at")||!!e.get("unlock_at"),hidden:!!e.get("hidden")}),togglePublishedState(){this.setState({published:!this.state.published,restricted:false,hidden:false})}}
t("YGE8")
v.openRestrictedDialog=function(){const e=d()("<div>").dialog({title:b.t("Editing permissions for: %{name}",{name:this.props.model.displayName()}),width:800,minHeight:300,close(){r.a.unmountComponentAtNode(this)
d()(this).remove()}})
t.e(109).then(t.bind(null,"Vm4Q")).then(i=>{let t=i.default
r.a.render(Object(a["a"])(t,{usageRightsRequiredForContext:this.props.usageRightsRequiredForContext,models:[this.props.model],closeDialog:()=>{e.dialog("close")}}),e[0])})}
var g=Object(a["a"])("i",{className:"icon-calendar-month icon-line"})
var y=Object(a["a"])("i",{className:"icon-off icon-line"})
var N=Object(a["a"])("i",{className:"icon-publish icon-Solid"})
var C=Object(a["a"])("i",{className:"icon-unpublish"})
var x=Object(a["a"])("i",{className:"icon-calendar-day"})
v.render=function(){const e=this.props.model&&this.props.model.displayName()||b.t("This file")
return this.props.userCanManageFilesForContext?this.state.published&&this.state.restricted?_.a.createElement("button",{type:"button","data-tooltip":"left",onClick:this.openRestrictedDialog,ref:"publishCloud",className:"btn-link published-status restricted",title:this.getRestrictedText(),"aria-label":b.t("%{fileName} is %{restricted} - Click to modify",{fileName:e,restricted:this.getRestrictedText()})},g):this.state.published&&this.state.hidden?_.a.createElement("button",{type:"button","data-tooltip":"left",onClick:this.openRestrictedDialog,ref:"publishCloud",className:"btn-link published-status hiddenState",title:b.t("Not visible in student files"),"aria-label":b.t("%{fileName} is not visible in student files - Click to modify",{fileName:e})},y):this.state.published?_.a.createElement("button",{type:"button","data-tooltip":"left",onClick:this.openRestrictedDialog,ref:"publishCloud",className:"btn-link published-status published",title:b.t("Published"),"aria-label":b.t("%{fileName} is Published - Click to modify",{fileName:e})},N):_.a.createElement("button",{type:"button","data-tooltip":"left",onClick:this.openRestrictedDialog,ref:"publishCloud",className:"btn-link published-status unpublished",title:b.t("Unpublished"),"aria-label":b.t("%{fileName} is Unpublished - Click to modify",{fileName:e})},C):this.state.published&&this.state.restricted?_.a.createElement("div",{style:{marginRight:"12px"},"data-tooltip":"left",ref:"publishCloud",className:"published-status restricted",title:this.getRestrictedText(),"aria-label":b.t("%{fileName} is %{restricted}",{fileName:e,restricted:this.getRestrictedText()})},x):Object(a["a"])("div",{style:{width:28,height:36}})}
i["a"]=s()(v)},HaSH:function(e,i,t){"use strict"
t.d(i,"a",(function(){return l}))
var a=t("dfg0")
class l extends a["a"]{initialize(e,i){return super.initialize(...arguments)}}},M4Ft:function(e,i,t){"use strict"
t.d(i,"a",(function(){return l}))
var a="undefined"!==typeof navigator&&navigator.userAgent||""
var l=/msie|trident/i.test(a)},Yi8D:function(e,i,t){"use strict"
t.d(i,"a",(function(){return s}))
var a=t("btHx")
var l=t("GLiE")
var _=t.n(l)
var n=t("jFQ7")
class s extends a["a"]{initialize(){this.on("change:sort change:order",this.setQueryStringParams)
return super.initialize(...arguments)}fetch(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:{}
e.data=_.a.extend({content_types:null!=this.parentFolder?this.parentFolder.contentTypes:void 0},e.data||{});(null!=this.parentFolder?this.parentFolder.useVerifiers:void 0)&&(e.data.use_verifiers=1)
return super.fetch(e)}parse(e){if(e&&this.parentFolder){const i=this.parentFolder.previewUrl()
_.a.each(e,e=>e.rce_preview_url=i?i.replace("{{id}}",e.id.toString()):e.url)}return super.parse(...arguments)}setQueryStringParams(){const e={include:["user"],per_page:20,sort:this.get("sort"),order:this.get("order")}
if(this.loadedAll)return
const i=new URL(this.url)
const t=deparam(i.search)
i.search=$.param(_.a.extend(t,e))
this.url=i.toString()
return this.reset()}}s.optionProperty("parentFolder")
s.prototype.model=n["a"]},dfg0:function(e,i,t){"use strict"
var a=t("FIFq")
var l=t.n(a)
var _=t("GLiE")
var n=t.n(_)
var s=t("Cf7h")
var o=function(e,i){for(var t in i)r.call(i,t)&&(e[t]=i[t])
function a(){this.constructor=e}a.prototype=i.prototype
e.prototype=new a
e.__super__=i.prototype
return e},r={}.hasOwnProperty
i["a"]=function(e){o(i,e)
function i(){return i.__super__.constructor.apply(this,arguments)}i.prototype.displayName=function(){return this.get("display_name")||this.get("name")}
i.prototype.destinationIsSameContext=function(e){var i,t,a,l,_,n,o,r
o=(i=this.get("context_asset_string"))?Object(s["a"])(i,false):[null!=(l=this.collection.parentFolder)?l.get("context_type"):void 0,null!=(_=this.collection.parentFolder)&&null!=(n=_.get("context_id"))?n.toString():void 0],a=o[0],t=o[1]
return a&&t&&a.toLowerCase()===e.get("context_type").toLowerCase()&&t===(null!=(r=e.get("context_id"))?r.toString():void 0)}
i.prototype.moveTo=function(e,i){null==i&&(i={})
return this.destinationIsSameContext(e)?this.moveToFolder(e,i):this.copyToContext(e,i)}
i.prototype.moveToFolder=function(e,i){var t
null==i&&(i={})
t=this.setAttributes({parent_folder_id:e.id},i)
$.extend(t,{parent_folder_id:e.id})
return this.save({},{attrs:t}).then((a=this,function(){a.collection.remove(a)
return a.updateCollection(a,e,i)}))
var a}
i.prototype.copyToContext=function(e,i){var t,a,l,_,s,o
null==i&&(i={})
t=this.setAttributes($.extend({},this.attributes),i)
s=this.isFile?"file":"folder"
t["source_"+s+"_id"]=t.id
delete t.id
a=new this.constructor(n.a.omit(t,"id","parent_folder_id","parent_folder_path"))
l=this.updateCollection(a,e,i)
a.url=l.url
this.set("url",l.url)
_="copy_"+s
o="/api/v1/folders/"+e.attributes.id+"/"+_
return a.save(t,{url:o})}
i.prototype.setAttributes=function(e,i){null==e&&(e={})
null==i&&(i={})
"overwrite"===i.dup?$.extend(e,{on_duplicate:"overwrite"}):"rename"===i.dup&&(i.name?$.extend(e,{display_name:i.name,name:i.name,on_duplicate:"rename"}):$.extend(e,{on_duplicate:"rename"}))
return e}
i.prototype.updateCollection=function(e,i,t){var a,l
l=this.isFile?"files":"folders"
a=i[l]
"overwrite"===t.dup&&a.remove(a.where({display_name:e.get("display_name")}))
a.add(e,{merge:true})
return a}
return i}(l.a.Model)},jFQ7:function(e,i,t){"use strict"
var a=t("ouhR")
var l=t.n(a)
var _=t("GLiE")
var n=t.n(_)
var s=t("dfg0")
var o=t("60Hp")
t("jYyc")
var r=function(e,i){return function(){return e.apply(i,arguments)}},c=function(e,i){for(var t in i)d.call(i,t)&&(e[t]=i[t])
function a(){this.constructor=e}a.prototype=i.prototype
e.prototype=new a
e.__super__=i.prototype
return e},d={}.hasOwnProperty,f=[].slice
i["a"]=function(e){c(i,e)
function i(){this.externalToolEnabled=r(this.externalToolEnabled,this)
return i.__super__.constructor.apply(this,arguments)}i.prototype.url=function(){return this.isNew()?i.__super__.url.apply(this,arguments):"/api/v1/files/"+this.id}
i.prototype.initialize=function(e,t){null==t&&(t={})
this.preflightUrl=t.preflightUrl
return i.__super__.initialize.apply(this,arguments)}
i.prototype.save=function(e,t){var a,_,n,s,r,c
null==e&&(e={})
null==t&&(t={})
if(!this.get("file"))return i.__super__.save.apply(this,arguments)
this.set(e)
a=l.a.Deferred()
r=(d=this,function(e){d.set(e)
a.resolve(e)
return"function"===typeof t.success?t.success(e):void 0})
var d
s=function(e){a.reject(e)
return"function"===typeof t.error?t.error(e):void 0}
_=this.get("file")
n=(_.value||_.name).split(/[\/\\]/).pop()
_=_.files[0]
c={name:n,on_duplicate:"rename"}
Object(o["uploadFile"])(this.preflightUrl,c,_).then(r)["catch"](s)
return a}
i.prototype.isFile=true
i.prototype.toJSON=function(){var e
if(!this.get("file"))return i.__super__.toJSON.apply(this,arguments)
return n.a.pick.apply(n.a,[this.attributes,"file"].concat(f.call(n.a.keys(null!=(e=this.uploadParams)?e:{}))))}
i.prototype.present=function(){return n.a.clone(this.attributes)}
i.prototype.externalToolEnabled=function(e){var i
if(e.accept_media_types&&e.accept_media_types.length>0){i=this.get("content-type")
return n.a.find(e.accept_media_types.split(","),(function(e){var t
t=new RegExp("^"+e.replace("*",".*")+"$")
return i.match(t)}))}return true}
return i}(s["a"])},lUQV:function(e,i,t){"use strict"
var a=t("17x9")
var l=t.n(a)
var _=t("mNVu")
var n=t("dfg0")
i["a"]={contextType:l.a.oneOf(["users","groups","accounts","courses"]),contextId:l.a.oneOfType([l.a.string,l.a.number]),folder:l.a.instanceOf(_["a"]),filesystemObject:l.a.instanceOf(n["a"])}},mNVu:function(e,i,t){"use strict"
var a=t("dfg0")
t("FIFq")
var l=t("GLiE")
var _=t.n(l)
var n={}
var s=function(e){var i=_.a.uniqueId()
var t=_.a.extend((function(t,a){var l=function(){return new e(t,a)}
var _=t&&t[e.prototype.idAttribute]
if(_){var s=i+":"+_
if(n[s]){var o=n[s]
a&&a.parse&&(t=o.parse(t))
o.set(t)}else n[s]=l()
return n[s]}var r=l()
r.on("change:"+e.prototype.idAttribute,(function(e,t){n[i+":"+t]=r
r.off(null,null,this)}),this)
return r}),e)
t.prototype=e.prototype
return t}
s.resetCache=function(){n={}}
var o=s
var r=t("btHx")
var c=t("Yi8D")
var d=t("yE80")
var f={encodeSpecialChars:e=>e.replace(/%/g,"&#37;"),decodeSpecialChars:e=>e.split("/").map(e=>encodeURIComponent(decodeURIComponent(e).replace(/&#37;/,"%"))).join("/")}
const u=/^[^\/]+\/?/
let b=null
function m(e,i){return"name"!==i||e instanceof k?"user"===i?v(e.get("user"),e=>e.display_name)||"":"usage_rights"===i?v(e.get("usage_rights"),e=>e.license_name)||"":e.get(i):e.get("display_name")}class p extends a["a"]{initialize(e){this.contentTypes||(this.contentTypes=null!=e?e.contentTypes:void 0)
this.useVerifiers||(this.useVerifiers=null!=e?e.useVerifiers:void 0)
this.setUpFilesAndFoldersIfNeeded()
this.on("change:sort change:order",this.setQueryStringParams)
return super.initialize(...arguments)}url(){return this.isNew()?super.url(...arguments):"/api/v1/folders/".concat(this.id)}parse(e){const i=super.parse(...arguments)
this.contentTypes||(this.contentTypes=e.contentTypes)
this.useVerifiers||(this.useVerifiers=e.useVerifiers)
this.setUpFilesAndFoldersIfNeeded()
this.folders.url=e.folders_url
this.files.url=e.files_url
return i}setUpFilesAndFoldersIfNeeded(){this.folders||(this.folders=new h([],{parentFolder:this}))
if(!this.files)return this.files=new c["a"]([],{parentFolder:this})}getSubtrees(){return this.folders}getItems(){return this.files}expand(){let e=arguments.length>0&&void 0!==arguments[0]&&arguments[0]
let i=arguments.length>1&&void 0!==arguments[1]?arguments[1]:{}
let t
this.isExpanded=true
this.trigger("expanded")
if(this.expandDfd||e)return $.when()
this.isExpanding=true
this.trigger("beginexpanding")
this.expandDfd=$.Deferred().done(()=>{this.isExpanding=false
return this.trigger("endexpanding")})
const a=this.folders.url===this.folders.constructor.prototype.url||this.files.url===this.files.constructor.prototype.url;(a||e)&&(t=this.fetch())
return $.when(t).done(()=>{let e,t
0!==this.get("folders_count")&&(t=this.folders.fetch())
0===this.get("files_count")||i.onlyShowSubtrees||(e=this.files.fetch())
return $.when(t,e).done(this.expandDfd.resolve)})}collapse(){this.isExpanded=false
return this.trigger("collapsed")}toggle(e){return this.isExpanded?this.collapse():this.expand(false,e)}previewUrl(){let e
if(e=this.get("context_type"),["Course","Group"].includes(e))return"/".concat("".concat(this.get("context_type").toLowerCase(),"s"),"/",this.get("context_id"),"/files/{{id}}/preview")}isEmpty(){return!!(this.files.loadedAll&&0===this.files.length)&&this.folders.loadedAll&&0===this.folders.length}urlPath(){let e=(this.get("full_name")||"").replace(u,"")
e=f.encodeSpecialChars(e)
e=e.split("/").map(e=>encodeURIComponent(e)).join("/")
b||(b=t("BHWx").default)
if(b.showingAllContexts){const i="".concat(v(this.get("context_type"),e=>e.toLowerCase()),"s_").concat(this.get("context_id"))
e="".concat(i,"/").concat(e)}return e}childrenSorter(){let e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:"name"
let i=arguments.length>1&&void 0!==arguments[1]?arguments[1]:"asc"
let t=arguments.length>2?arguments[2]:void 0
let a=arguments.length>3?arguments[3]:void 0
let l
const _=["name","user","usage_rights"].includes(e)
t=m(t,e)
a=m(a,e)
l=_?d["a"].strings(t,a):(()=>{if(t===a)return 0
if(t>a||void 0===t)return 1
if(t<a||void 0===a)return-1
throw new Error("wat? error sorting")})()
"desc"===i&&(l=0-l)
return l}children(e){let i=e.sort,t=e.order
return this.folders.toArray().concat(this.files.toArray()).sort(this.childrenSorter.bind(null,i,t))}}p.resolvePath=function(e,i,t){t=f.decodeSpecialChars(t)
const a="/api/v1/".concat(e,"/").concat(i,"/folders/by_path").concat(t)
return $.getJSON(a).pipe(e=>e.map(e=>new k(e,{parse:true})))}
p.prototype.defaults={name:""}
const k=o(p)
i["a"]=k
class h extends r["a"]{static initClass(){this.optionProperty("parentFolder")
this.prototype.model=k}parse(e){e&&e.forEach(e=>{e.contentTypes=this.parentFolder.contentTypes
return e.useVerifiers=this.parentFolder.useVerifiers})
return super.parse(...arguments)}}h.initClass()
k.FoldersCollection=h
function v(e,i){return"undefined"!==typeof e&&null!==e?i(e):void 0}},yE80:function(e,i,t){"use strict"
var a=t("pQTu")
i["a"]={strings(e,i){let t=a["default"].locale||"en-US"
const l={zh_Hant:"zh-Hant"}
t=l[t]||t
return e.localeCompare(i,t,{sensitivity:"variant",ignorePunctuation:false,numeric:true})},by(e){return(i,t)=>this.strings(e(i),e(t))},byKey(e){return this.by(i=>i[e])},byGet(e){return this.by(i=>i.get(e))}}}}])

//# sourceMappingURL=69-c-2d3d6fe688.js.map