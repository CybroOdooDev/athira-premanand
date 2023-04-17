 /** @odoo-module **/
import { registry } from "@web/core/registry";
import { useInputField } from "@web/views/fields/input_field_hook";
import { isBinarySize } from "@web/core/utils/binary";
import { url } from "@web/core/utils/urls";
import basic_fields from 'web.basic_fields';
import {ImageField, imageCacheKey} from "@web/views/fields/image/image_field";
import time from 'web.time';
var translation = require('web.translation');
var _t = translation._t;
var FieldImage = basic_fields.image1920;
const { Component,useEffect, onMounted, useState} = owl;

export class Field3D extends ImageField {
   setup(){
    super.setup();
    this.elId = `#${this.props.name}_el`
    this.state = useState({
        isValid: true,
        value: url('/model_viewer_widget/static/src/assets/3d.glb')
    });
    this.canvasEl = '<canvas class="view3d-canvas"/>'
    useEffect(() => {
        this.createCanvas()
        if (isBinarySize(this.props.value)) {
            this.state.value = url("/web/content", {
                model: this.props.record.resModel,
                id: this.props.record.resId,
                field: this.props.name,
                unique: imageCacheKey(this.rawCacheKey),
            });
        } else if(this.props.value){
            this.state.value = `data:model/gltf-binary;base64, ${this.props.value}`
        }
        this.view3D = new View3D(this.elId, {
            src: this.state.value
        });
    })
   }
   onFileRemove(){
    console.log(this.view3D)
    super.onFileRemove();
    this.createCanvas()
    this.state.value = url('/model_viewer_widget/static/src/assets/3d.glb');
    if(this.view3D){
        this.view3D.load(this.state.value)
    }
   }
   createCanvas(){
       var elem = document.querySelector(this.elId);
       const prevCanvas = elem.querySelector('canvas');
       if(prevCanvas)
           elem.removeChild(prevCanvas)
       const canvas = document.createElement('canvas');
       canvas.width = 600;
       canvas.height = 500;
       canvas.classList.add('view3d-canvas')
       elem.appendChild(canvas);
   }
}
Field3D.acceptedFileExtensions = "*"
Field3D.template = "Field3DWidget"

registry.category("fields").add("3D_widget", Field3D);
