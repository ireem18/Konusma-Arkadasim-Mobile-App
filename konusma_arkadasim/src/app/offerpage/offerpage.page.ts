import { Component, OnInit } from '@angular/core';
import { UserService } from '../api/user.service';
import { UploadingService } from  '../uploading.service';
import { FileUploader, FileLikeObject } from  'ng2-file-upload';
import { concat } from  'rxjs';
import {Media,MediaObject} from "@ionic-native/media/ngx";
import {File} from "@ionic-native/file/ngx";
import {FileTransfer,FileUploadOptions,FileTransferObject} from '@ionic-native/file-transfer/ngx';
import {FileChooser} from '@ionic-native/file-chooser/ngx';
import {FilePath} from '@ionic-native/file-path/ngx';

@Component({
  selector: 'app-offerpage',
  templateUrl: './offerpage.page.html',
  styleUrls: ['./offerpage.page.scss'],
})
export class OfferpagePage implements OnInit {

  userDetails:any =[];
  userDetailsDJANGO:any =[];
  status:string = "";
  audioFile:MediaObject = this.media.create(this.file.externalRootDirectory+'/word.wav');
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

  constructor(private userService:UserService,private media:Media,private file:File,private transfer:FileTransfer,private filePath:FilePath,private fileChooser:FileChooser,private uploadingService: UploadingService) 
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
 
     ++this.timer;
 
     if (this.timer<0){
       this.startTimer();
     }
 
    }
  

  GetUserDetailsDJANGO(){
    this.userService.GetUsersDJANGO().subscribe((users)=>{
      var anyData2 = <any>users;
      this.userDetailsDJANGO = anyData2.users;
      console.log(anyData2.users);
      
    })
  }
}
