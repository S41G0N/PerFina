from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import StreamingResponse
from schemas.user_schema import InvoiceData
from services.generate_invoice import generate_invoice
from models.user_model import User
from services.authentication_service import get_current_user

router = APIRouter()


@router.post("/generate-invoice")
async def create_invoice(
    invoice_data: InvoiceData, current_user: User = Depends(get_current_user)
):
    try:
        pdf_buffer = generate_invoice(
            company_name=invoice_data.company_name,
            company_address=invoice_data.company_address,
            company_postal_code=invoice_data.company_postal_code,
            company_phone=invoice_data.company_phone,
            company_email=invoice_data.company_email,
            company_ico=invoice_data.company_ico,
            company_dic=invoice_data.company_dic,
            company_bank_account=invoice_data.company_bank_account,
            category=invoice_data.category,
            services=invoice_data.services,
            rate=invoice_data.rate,
            hours=invoice_data.hours,
            invoice_number=invoice_data.invoice_number,
            variable_symbol=invoice_data.variable_symbol,
            invoice_date=invoice_data.invoice_date,
            invoice_due=invoice_data.invoice_due,
            client_name=invoice_data.client_name,
            client_address=invoice_data.client_address,
            client_postal_code=invoice_data.client_postal_code,
            client_ico=invoice_data.client_ico,
            client_dic=invoice_data.client_dic,
        )
        return StreamingResponse(
            pdf_buffer,
            media_type="application/pdf",
            headers={"Content-Disposition": "attachment; filename=invoice.pdf"},
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
