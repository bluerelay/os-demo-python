import { Component, OnInit } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { of } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { MatSnackBar, MatDialog } from '@angular/material';
import { MessageComponent } from './message.component';

export interface MessageData {
  author: string,
  content: string
}

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {
  title = 'testui';
  private headers = new HttpHeaders({ 'Content-Type': 'application/json' });
  messages: MessageData[] = [];

  constructor(
    private http: HttpClient,
    private snackBar: MatSnackBar,
    public dialog: MatDialog
  ) { }

  ngOnInit() {
    this.http.get<MessageData[]>(`/messages`, {
      headers: this.headers,
      observe: 'body',
      responseType: 'json'
    }).pipe(
      catchError(val => {
        return of([{author: '', message: 'oops... something is broken!'}]);
      })
    ).subscribe((data: MessageData[]) => {
      this.messages = data;
    });
  }

  add() {
    let dialogRef = this.dialog.open(MessageComponent, {
      width: '400px'
    });

    dialogRef.afterClosed().subscribe((message: MessageData) => {
      if (message) {
        this.http.post<any>(`/message`, message, {
          headers: this.headers,
          observe: 'body',
          responseType: 'json'
        }).subscribe(
          (result: any) => {
            if(result.success) {
              this.snackBar.open('Comment saved!', '', {
                duration: 2000,
              });
              this.messages.unshift(result.message);
            } else {
              this.snackBar.open('Failed, please try again!', '', {
                duration: 3000,
              });
            }
          }
        );
      }
    });
  }
}
