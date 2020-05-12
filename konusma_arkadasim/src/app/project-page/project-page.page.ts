import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import {OfferpagePage} from '../offerpage/offerpage.page';
import {Media,MediaObject} from "@ionic-native/media/ngx";
import {File} from "@ionic-native/file/ngx";
import { BehaviorSubject } from 'rxjs';
import {FileTransfer,FileUploadOptions,FileTransferObject} from '@ionic-native/file-transfer/ngx';
import {FileChooser} from '@ionic-native/file-chooser/ngx';
import {FilePath} from '@ionic-native/file-path/ngx';

import { UploadingService } from  '../uploading.service';
import { FileUploader, FileLikeObject } from  'ng2-file-upload';
import { concat } from  'rxjs';

@Component({
  selector: 'app-project-page',
  templateUrl: './project-page.page.html',
  styleUrls: ['./project-page.page.scss'],
})
export class ProjectPagePage implements OnInit {
 
  status:string = "";
  audioFile:MediaObject = this.media.create(this.file.externalRootDirectory+'/story.wav');
  time : BehaviorSubject<string> = new BehaviorSubject('00:00');
  timer : number; // seconds
  timeArray :any= [];
  timer2 : number;
  interval;
  state = 'start';
  uploadText:any;
  dowloadText:any;
  fileTransfer:FileTransferObject;

  public fileUploader: FileUploader = new FileUploader({});
  public hasBaseDropZoneOver: boolean = false;

  constructor(private router: Router,private media:Media,private file:File,private transfer:FileTransfer,private filePath:FilePath,private fileChooser:FileChooser,private uploadingService: UploadingService) 
  { 
    this.uploadText = "";
    this.dowloadText = "";

  }
  ngOnInit() {
  }

  fileOverBase(event): void {
    this.hasBaseDropZoneOver = event;
  }

  getFiles(): FileLikeObject[] {
    return this.fileUploader.queue.map((fileItem) => {
      return fileItem.file;

    });
  }

  uploadFiles() {
    
    let files = this.getFiles();
    let requests = [];

    files.forEach((file) => {
      let formData = new FormData();
      formData.append('file' , file.rawFile, file.name);
      requests.push(this.uploadingService.uploadFormData(formData));

    });

    concat(...requests).subscribe(
      (res) => {
        console.log(res);
      },
      (err) => {  
        console.log(err);
      }
    );
  }

  goOfferPage(){
    this.router.navigate(['offerpage']);
  }
  RecordAudio(){
    this.audioFile.startRecord();
    this.status = "kayıt..."
    this.startTimer();
  }
  StopRecording(){
    this.audioFile.stopRecord();
    this.status = "kaydedildi..."
    this.stopTimer();
    setTimeout(() => 
    {
      this.uploadFiles();
    },5000);
    
  }

  startTimer(){
    this.state ='start';
    clearInterval(this.interval);
    this.timer = 0;
    this.updateTimeValue();
    this.interval = setInterval( () => {
      this.updateTimeValue();
    }, 1000);
  }
  stopTimer(){
    clearInterval(this.interval);
    this.time.next('00:00');
  
   }
 
   DurationTimer(){
     let minutes :any = this.timer / 60;
     let seconds :any = this.timer % 60;
 
     minutes = String ('0' + Math.floor(minutes)).slice(-2);
     seconds = String ('0' + Math.floor(seconds)).slice(-2);
 
     const text = minutes + ':' + seconds;
     console.log(text);
     this.status = "duraklama noktası alındı..."
    }
 
   updateTimeValue(){
     let minutes :any = this.timer / 60;
     let seconds :any = this.timer % 60;
 
     minutes = String ('0' + Math.floor(minutes)).slice(-2);
     seconds = String ('0' + Math.floor(seconds)).slice(-2);
 
     const text = minutes + ':' + seconds;
     this.time.next(text);
 
     ++this.timer;
 
     if (this.timer<0){
       this.startTimer();
     }
 
   }

}

/*
  UploadFile()
  {
    this.fileChooser.open().then((uri) =>{
      this.filePath.resolveNativePath(uri).then(
      (nativepath)=>{
          this.fileTransfer = this.transfer.create();
          let options:FileUploadOptions = {
            fileKey:'videofile',
            fileName:'video.mp4',
            chunkedMode:false,
            headers:{},
            mimeType:'video/mp4'
          }
          this.uploadText = "uploading...";
          this.fileTransfer.upload(nativepath,'your endpoint api url',options).then((data)=>
          {
              alert("transfer done="+JSON.stringify(data) );
              this.uploadText= "";
          },(err)=>{
            this.uploadText = "";
          })
      },(err)=>{
        alert(JSON.stringify(err));
      })
    },(err)=>{
      alert(JSON.stringify(err));
    })
  }

AbortUpload(){
  this.fileTransfer.abort;
  alert("upload cancel" );
}
*/