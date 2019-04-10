import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { AppRoutingModule } from './app-routing.module';
import { MatModule } from './mat.module';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { MessageComponent } from './message.component';
import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    MessageComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    MatModule,
    CommonModule,
    FormsModule,
    BrowserAnimationsModule
  ],
  providers: [],
  entryComponents: [
    MessageComponent
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
