import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { PageKayitPage } from './page-kayit.page';

describe('PageKayitPage', () => {
  let component: PageKayitPage;
  let fixture: ComponentFixture<PageKayitPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PageKayitPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(PageKayitPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
