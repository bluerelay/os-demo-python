import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material';

import { MessageData } from './app.component';

@Component({
  selector: 'app-message',
  templateUrl: './message.component.html'
})
export class MessageComponent {
  message: MessageData = {author: '', content: ''};

  constructor(
    public dialogRef: MatDialogRef<MessageComponent>
  ) { }

  onSubmit() {
    this.dialogRef.close(this.message);
  }

  onCancel() {
    this.dialogRef.close();
  }
}